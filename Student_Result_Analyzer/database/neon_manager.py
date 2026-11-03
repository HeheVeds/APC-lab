"""
Neon PostgreSQL Database Manager Module
Handles cloud PostgreSQL database connections, schema migrations,
and synchronization with Neon (serverless Postgres) for the Student Result Analyzer.
"""
import os
import psycopg2
from psycopg2.extras import execute_values
import pandas as pd
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class NeonDatabaseManager:
    """
    Manages connections and operations with Neon Serverless PostgreSQL.
    """

    def __init__(self, connection_string: str = None):
        self.connection_url = connection_string or os.getenv("NEON_DATABASE_URL", "")

    def get_connection(self):
        """Creates and returns a connection to the Neon cloud PostgreSQL database."""
        if not self.connection_url:
            raise ValueError(
                "NEON_DATABASE_URL is not set. Please add your Neon connection string to the .env file."
            )
        return psycopg2.connect(self.connection_url)

    def test_connection(self) -> dict:
        """Tests connection to Neon and returns server details."""
        try:
            with self.get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute("SELECT version();")
                    db_version = cur.fetchone()[0]
                    cur.execute("SELECT current_database(), current_user;")
                    db_name, db_user = cur.fetchone()
            return {
                "status": "Success",
                "message": "Connected to Neon PostgreSQL successfully!",
                "database": db_name,
                "user": db_user,
                "version": db_version
            }
        except Exception as e:
            return {
                "status": "Error",
                "message": f"Connection failed: {str(e)}"
            }

    def create_tables(self) -> dict:
        """Creates the relational PostgreSQL tables in Neon."""
        try:
            with self.get_connection() as conn:
                with conn.cursor() as cur:
                    # 1. Students Table
                    cur.execute("""
                        CREATE TABLE IF NOT EXISTS students (
                            roll_no VARCHAR(20) PRIMARY KEY,
                            name VARCHAR(100) NOT NULL,
                            department VARCHAR(50) DEFAULT 'Computer Science',
                            gender VARCHAR(20) DEFAULT 'Unspecified',
                            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                        );
                    """)

                    # 2. Semester Marks Table
                    cur.execute("""
                        CREATE TABLE IF NOT EXISTS semester_marks (
                            id SERIAL PRIMARY KEY,
                            roll_no VARCHAR(20) REFERENCES students(roll_no) ON DELETE CASCADE,
                            semester VARCHAR(30) NOT NULL,
                            subject VARCHAR(100) NOT NULL,
                            marks NUMERIC(5, 2) NOT NULL,
                            max_marks NUMERIC(5, 2) DEFAULT 100.0,
                            status VARCHAR(10) NOT NULL,
                            UNIQUE(roll_no, semester, subject)
                        );
                    """)

                    # 3. Supplementary Exams Table
                    cur.execute("""
                        CREATE TABLE IF NOT EXISTS supplementary_exams (
                            id SERIAL PRIMARY KEY,
                            roll_no VARCHAR(20) REFERENCES students(roll_no) ON DELETE CASCADE,
                            exam_type VARCHAR(30) NOT NULL,
                            semester VARCHAR(30) NOT NULL,
                            subject VARCHAR(100) NOT NULL,
                            original_marks NUMERIC(5, 2),
                            attempt_marks NUMERIC(5, 2),
                            backup_marks NUMERIC(5, 2),
                            status VARCHAR(20) NOT NULL
                        );
                    """)

                    # 4. Academic Summaries Table
                    cur.execute("""
                        CREATE TABLE IF NOT EXISTS academic_summaries (
                            roll_no VARCHAR(20) PRIMARY KEY REFERENCES students(roll_no) ON DELETE CASCADE,
                            sem1_pct NUMERIC(5, 2),
                            sem2_pct NUMERIC(5, 2),
                            sem3_pct NUMERIC(5, 2),
                            cumulative_pct NUMERIC(5, 2),
                            grade VARCHAR(30),
                            status VARCHAR(30),
                            active_backlogs INTEGER DEFAULT 0,
                            last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                        );
                    """)

                    # Indexes
                    cur.execute("CREATE INDEX IF NOT EXISTS idx_neon_marks_roll ON semester_marks(roll_no);")
                    cur.execute("CREATE INDEX IF NOT EXISTS idx_neon_supp_roll ON supplementary_exams(roll_no);")

                    conn.commit()
            return {"status": "Success", "message": "All PostgreSQL tables created in Neon successfully."}
        except Exception as e:
            return {"status": "Error", "message": f"Table creation failed: {str(e)}"}

    def sync_from_csv(self, sem1_path: str, sem2_path: str, sem3_path: str,
                      makeup_path: str = None, backup_path: str = None) -> dict:
        """Loads all CSV academic records into Neon PostgreSQL tables."""
        try:
            self.create_tables()

            with self.get_connection() as conn:
                with conn.cursor() as cur:
                    non_sub = {"Roll_No", "Name", "Department", "Gender"}
                    sem_configs = [
                        ("Semester 1", sem1_path),
                        ("Semester 2", sem2_path),
                        ("Semester 3", sem3_path)
                    ]

                    for sem_name, fpath in sem_configs:
                        if not os.path.exists(fpath):
                            continue
                        df = pd.read_csv(fpath)
                        subject_cols = [c for c in df.columns if c not in non_sub]

                        for _, row in df.iterrows():
                            roll = str(row["Roll_No"]).strip()
                            name = str(row["Name"]).strip()
                            dept = str(row.get("Department", "Computer Science")).strip()
                            gender = str(row.get("Gender", "Unspecified")).strip()

                            # Upsert Student
                            cur.execute("""
                                INSERT INTO students (roll_no, name, department, gender)
                                VALUES (%s, %s, %s, %s)
                                ON CONFLICT(roll_no) DO UPDATE SET
                                    name = EXCLUDED.name,
                                    department = EXCLUDED.department,
                                    gender = EXCLUDED.gender;
                            """, (roll, name, dept, gender))

                            # Upsert Marks
                            for sub in subject_cols:
                                if pd.notnull(row[sub]):
                                    val = float(row[sub])
                                    status = "PASS" if val >= 40.0 else "FAIL"
                                    cur.execute("""
                                        INSERT INTO semester_marks (roll_no, semester, subject, marks, max_marks, status)
                                        VALUES (%s, %s, %s, %s, 100.0, %s)
                                        ON CONFLICT(roll_no, semester, subject) DO UPDATE SET
                                            marks = EXCLUDED.marks,
                                            status = EXCLUDED.status;
                                    """, (roll, sem_name, sub, val, status))

                    # Makeup Exam
                    if makeup_path and os.path.exists(makeup_path):
                        m_df = pd.read_csv(makeup_path)
                        for _, row in m_df.iterrows():
                            cur.execute("""
                                INSERT INTO supplementary_exams 
                                (roll_no, exam_type, semester, subject, original_marks, attempt_marks, status)
                                VALUES (%s, 'Makeup Exam', %s, %s, %s, %s, %s);
                            """, (
                                str(row["Roll_No"]).strip(),
                                str(row.get("Semester", "Unknown")).strip(),
                                str(row.get("Subject", "Unknown")).strip(),
                                float(row.get("Original_Marks", 0)),
                                float(row.get("Makeup_Marks", 0)),
                                str(row.get("Status", "Unknown")).strip()
                            ))

                    # Backup Exam
                    if backup_path and os.path.exists(backup_path):
                        b_df = pd.read_csv(backup_path)
                        for _, row in b_df.iterrows():
                            cur.execute("""
                                INSERT INTO supplementary_exams 
                                (roll_no, exam_type, semester, subject, original_marks, attempt_marks, backup_marks, status)
                                VALUES (%s, 'Backup Exam', %s, %s, %s, %s, %s, %s);
                            """, (
                                str(row["Roll_No"]).strip(),
                                str(row.get("Semester", "Unknown")).strip(),
                                str(row.get("Subject", "Unknown")).strip(),
                                float(row.get("Original_Marks", 0)),
                                float(row.get("Makeup_Marks", 0)),
                                float(row.get("Backup_Marks", 0)),
                                str(row.get("Status", "Unknown")).strip()
                            ))

                    conn.commit()

            # Materialize summaries
            self._refresh_summaries()
            return {"status": "Success", "message": "All student records migrated to Neon successfully!"}
        except Exception as e:
            return {"status": "Error", "message": f"Sync failed: {str(e)}"}

    def _refresh_summaries(self):
        """Recalculates SGPA, CGPA, and backlog metrics in Neon."""
        with self.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT roll_no FROM students;")
                rolls = [r[0] for r in cur.fetchall()]

                for roll in rolls:
                    # Sem 1, 2, 3 averages
                    cur.execute("""
                        SELECT 
                            ROUND(AVG(CASE WHEN semester = 'Semester 1' THEN marks END), 2) AS s1,
                            ROUND(AVG(CASE WHEN semester = 'Semester 2' THEN marks END), 2) AS s2,
                            ROUND(AVG(CASE WHEN semester = 'Semester 3' THEN marks END), 2) AS s3,
                            ROUND(AVG(marks), 2) AS cum,
                            COUNT(CASE WHEN marks < 40 THEN 1 END) AS failed
                        FROM semester_marks
                        WHERE roll_no = %s;
                    """, (roll,))
                    row = cur.fetchone()
                    s1, s2, s3, cum, failed = row
                    cum = float(cum or 0)
                    failed = int(failed or 0)

                    # Grade
                    if cum >= 90: grade = "O (Outstanding)"
                    elif cum >= 80: grade = "A+ (Excellent)"
                    elif cum >= 70: grade = "A (Very Good)"
                    elif cum >= 60: grade = "B+ (Good)"
                    elif cum >= 50: grade = "B (Above Average)"
                    elif cum >= 40: grade = "C (Pass)"
                    else: grade = "F (Fail)"

                    status = "PASS" if failed == 0 else "ATKT / BACKLOG"

                    cur.execute("""
                        INSERT INTO academic_summaries 
                        (roll_no, sem1_pct, sem2_pct, sem3_pct, cumulative_pct, grade, status, active_backlogs)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                        ON CONFLICT(roll_no) DO UPDATE SET
                            sem1_pct = EXCLUDED.sem1_pct,
                            sem2_pct = EXCLUDED.sem2_pct,
                            sem3_pct = EXCLUDED.sem3_pct,
                            cumulative_pct = EXCLUDED.cumulative_pct,
                            grade = EXCLUDED.grade,
                            status = EXCLUDED.status,
                            active_backlogs = EXCLUDED.active_backlogs,
                            last_updated = CURRENT_TIMESTAMP;
                    """, (roll, s1, s2, s3, cum, grade, status, failed))

                conn.commit()

    def fetch_all_students_df(self) -> pd.DataFrame:
        """Retrieves all students and their cumulative results from Neon."""
        query = """
            SELECT 
                s.roll_no AS "Roll No",
                s.name AS "Name",
                s.department AS "Department",
                s.gender AS "Gender",
                a.sem1_pct AS "Sem 1 %",
                a.sem2_pct AS "Sem 2 %",
                a.sem3_pct AS "Sem 3 %",
                a.cumulative_pct AS "Cumulative %",
                a.grade AS "Grade",
                a.status AS "Status",
                a.active_backlogs AS "Active Backlogs"
            FROM students s
            LEFT JOIN academic_summaries a ON s.roll_no = a.roll_no
            ORDER BY s.roll_no ASC;
        """
        with self.get_connection() as conn:
            return pd.read_sql_query(query, conn)
