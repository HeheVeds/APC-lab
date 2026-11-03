"""
Database Manager Module (Python SQLite3 & OOP)
Handles SQLite relational database creation, schema migrations,
CRUD operations, and seamless data loading between SQL and Pandas.
"""
import os
import sqlite3
from typing import Dict, List, Optional, Tuple
import pandas as pd


class DatabaseManager:
    """
    Manages SQLite database connections, schema creation, data insertion,
    and optimized relational querying for the Student Result & Performance Analyzer.
    """

    def __init__(self, db_path: Optional[str] = None):
        if db_path is None:
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            self.db_path = os.path.join(base_dir, "data", "student_records.db")
        else:
            self.db_path = db_path
            
        # Ensure parent directory exists
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        self.init_db()

    def get_connection(self) -> sqlite3.Connection:
        """Returns a connection to the SQLite database with Foreign Key support enabled."""
        conn = sqlite3.connect(self.db_path)
        conn.execute("PRAGMA foreign_keys = ON;")
        conn.row_factory = sqlite3.Row
        return conn

    def init_db(self) -> None:
        """Creates the relational database schema if it does not already exist."""
        with self.get_connection() as conn:
            cursor = conn.cursor()

            # 1. Students Table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS students (
                    roll_no TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    department TEXT NOT NULL DEFAULT 'Computer Science',
                    gender TEXT DEFAULT 'Unspecified',
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)

            # 2. Semester Marks Table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS semester_marks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    roll_no TEXT NOT NULL,
                    semester TEXT NOT NULL,
                    subject TEXT NOT NULL,
                    marks REAL NOT NULL,
                    max_marks REAL DEFAULT 100.0,
                    status TEXT NOT NULL,
                    FOREIGN KEY (roll_no) REFERENCES students(roll_no) ON DELETE CASCADE,
                    UNIQUE(roll_no, semester, subject)
                );
            """)

            # 3. Supplementary Exams (Makeup & Backup) Table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS supplementary_exams (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    roll_no TEXT NOT NULL,
                    exam_type TEXT NOT NULL,
                    semester TEXT NOT NULL,
                    subject TEXT NOT NULL,
                    original_marks REAL,
                    attempt_marks REAL,
                    backup_marks REAL,
                    status TEXT NOT NULL,
                    FOREIGN KEY (roll_no) REFERENCES students(roll_no) ON DELETE CASCADE
                );
            """)

            # 4. Academic Summaries Table (Materialized aggregates for fast querying)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS academic_summaries (
                    roll_no TEXT PRIMARY KEY,
                    sem1_pct REAL,
                    sem2_pct REAL,
                    sem3_pct REAL,
                    cumulative_pct REAL,
                    grade TEXT,
                    status TEXT,
                    active_backlogs INTEGER,
                    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (roll_no) REFERENCES students(roll_no) ON DELETE CASCADE
                );
            """)

            # Create Indexes for performance
            cursor.execute("CREATE INDEX IF NOT EXISTS idx_marks_roll ON semester_marks(roll_no);")
            cursor.execute("CREATE INDEX IF NOT EXISTS idx_marks_sem ON semester_marks(semester);")
            cursor.execute("CREATE INDEX IF NOT EXISTS idx_supp_roll ON supplementary_exams(roll_no);")

            conn.commit()

    def sync_from_csv_files(
        self,
        sem1_path: str,
        sem2_path: str,
        sem3_path: str,
        makeup_path: Optional[str] = None,
        backup_path: Optional[str] = None
    ) -> Dict[str, str]:
        """
        Parses pre-existing CSV result files and populates the SQLite database tables.
        Uses SQL transactions for high performance and atomicity.
        """
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()

                # Process Semesters
                sem_configs = [
                    ("Semester 1", sem1_path),
                    ("Semester 2", sem2_path),
                    ("Semester 3", sem3_path)
                ]

                non_subject_cols = {"Roll_No", "Name", "Department", "Gender"}

                for sem_name, file_path in sem_configs:
                    if not os.path.exists(file_path):
                        continue
                    df = pd.read_csv(file_path)
                    subject_cols = [c for c in df.columns if c not in non_subject_cols]

                    for _, row in df.iterrows():
                        roll = str(row["Roll_No"]).strip()
                        name = str(row["Name"]).strip()
                        dept = str(row.get("Department", "Computer Science")).strip()
                        gender = str(row.get("Gender", "Unspecified")).strip()

                        # Insert student if not exists
                        cursor.execute("""
                            INSERT INTO students (roll_no, name, department, gender)
                            VALUES (?, ?, ?, ?)
                            ON CONFLICT(roll_no) DO UPDATE SET
                                name=excluded.name,
                                department=excluded.department,
                                gender=excluded.gender;
                        """, (roll, name, dept, gender))

                        # Insert semester marks
                        for sub in subject_cols:
                            if pd.notnull(row[sub]):
                                val = float(row[sub])
                                status = "PASS" if val >= 40.0 else "FAIL"
                                cursor.execute("""
                                    INSERT INTO semester_marks (roll_no, semester, subject, marks, max_marks, status)
                                    VALUES (?, ?, ?, ?, 100.0, ?)
                                    ON CONFLICT(roll_no, semester, subject) DO UPDATE SET
                                        marks=excluded.marks,
                                        status=excluded.status;
                                """, (roll, sem_name, sub, val, status))

                # Process Makeup Exam CSV
                if makeup_path and os.path.exists(makeup_path):
                    m_df = pd.read_csv(makeup_path)
                    for _, row in m_df.iterrows():
                        roll = str(row["Roll_No"]).strip()
                        sem = str(row.get("Semester", "Unknown")).strip()
                        sub = str(row.get("Subject", "Unknown")).strip()
                        orig = float(row.get("Original_Marks", 0))
                        attempt = float(row.get("Makeup_Marks", 0))
                        status = str(row.get("Status", "Unknown")).strip()

                        cursor.execute("""
                            INSERT INTO supplementary_exams (roll_no, exam_type, semester, subject, original_marks, attempt_marks, status)
                            VALUES (?, 'Makeup Exam', ?, ?, ?, ?, ?);
                        """, (roll, sem, sub, orig, attempt, status))

                # Process Backup Exam CSV
                if backup_path and os.path.exists(backup_path):
                    b_df = pd.read_csv(backup_path)
                    for _, row in b_df.iterrows():
                        roll = str(row["Roll_No"]).strip()
                        sem = str(row.get("Semester", "Unknown")).strip()
                        sub = str(row.get("Subject", "Unknown")).strip()
                        orig = float(row.get("Original_Marks", 0))
                        makeup = float(row.get("Makeup_Marks", 0))
                        backup = float(row.get("Backup_Marks", 0))
                        status = str(row.get("Status", "Unknown")).strip()

                        cursor.execute("""
                            INSERT INTO supplementary_exams (roll_no, exam_type, semester, subject, original_marks, attempt_marks, backup_marks, status)
                            VALUES (?, 'Backup Exam', ?, ?, ?, ?, ?, ?);
                        """, (roll, sem, sub, orig, makeup, backup, status))

                conn.commit()

            # Refresh materialized academic summaries
            self.refresh_academic_summaries()
            return {"status": "Success", "message": "Database synchronized successfully with CSV records."}

        except Exception as e:
            return {"status": "Error", "message": f"Database sync failed: {str(e)}"}

    def refresh_academic_summaries(self) -> None:
        """Calculates and updates cumulative percentages, grades, and backlogs in the database."""
        with self.get_connection() as conn:
            cursor = conn.cursor()

            # Retrieve distinct students
            cursor.execute("SELECT roll_no FROM students")
            students = [r["roll_no"] for r in cursor.fetchall()]

            for roll in students:
                # Semester 1
                cursor.execute("""
                    SELECT AVG(marks) as sem_pct, SUM(CASE WHEN marks < 40 THEN 1 ELSE 0 END) as failed_cnt
                    FROM semester_marks WHERE roll_no = ? AND semester = 'Semester 1'
                """, (roll,))
                r1 = cursor.fetchone()
                s1_pct = round(r1["sem_pct"], 2) if r1 and r1["sem_pct"] is not None else None

                # Semester 2
                cursor.execute("""
                    SELECT AVG(marks) as sem_pct, SUM(CASE WHEN marks < 40 THEN 1 ELSE 0 END) as failed_cnt
                    FROM semester_marks WHERE roll_no = ? AND semester = 'Semester 2'
                """, (roll,))
                r2 = cursor.fetchone()
                s2_pct = round(r2["sem_pct"], 2) if r2 and r2["sem_pct"] is not None else None

                # Semester 3
                cursor.execute("""
                    SELECT AVG(marks) as sem_pct, SUM(CASE WHEN marks < 40 THEN 1 ELSE 0 END) as failed_cnt
                    FROM semester_marks WHERE roll_no = ? AND semester = 'Semester 3'
                """, (roll,))
                r3 = cursor.fetchone()
                s3_pct = round(r3["sem_pct"], 2) if r3 and r3["sem_pct"] is not None else None

                # Cumulative & Active Backlogs
                cursor.execute("""
                    SELECT AVG(marks) as cum_pct, SUM(CASE WHEN marks < 40 THEN 1 ELSE 0 END) as total_failed
                    FROM semester_marks WHERE roll_no = ?
                """, (roll,))
                rcum = cursor.fetchone()
                cum_pct = round(rcum["cum_pct"], 2) if rcum and rcum["cum_pct"] is not None else 0.0
                total_failed = rcum["total_failed"] if rcum and rcum["total_failed"] is not None else 0

                # Determine Grade
                grade = self._calculate_grade(cum_pct)
                status = "PASS" if total_failed == 0 else "ATKT / BACKLOG"

                cursor.execute("""
                    INSERT INTO academic_summaries (roll_no, sem1_pct, sem2_pct, sem3_pct, cumulative_pct, grade, status, active_backlogs)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                    ON CONFLICT(roll_no) DO UPDATE SET
                        sem1_pct=excluded.sem1_pct,
                        sem2_pct=excluded.sem2_pct,
                        sem3_pct=excluded.sem3_pct,
                        cumulative_pct=excluded.cumulative_pct,
                        grade=excluded.grade,
                        status=excluded.status,
                        active_backlogs=excluded.active_backlogs,
                        last_updated=CURRENT_TIMESTAMP;
                """, (roll, s1_pct, s2_pct, s3_pct, cum_pct, grade, status, total_failed))

            conn.commit()

    @staticmethod
    def _calculate_grade(pct: float) -> str:
        if pct >= 90:
            return "O (Outstanding)"
        elif pct >= 80:
            return "A+ (Excellent)"
        elif pct >= 70:
            return "A (Very Good)"
        elif pct >= 60:
            return "B+ (Good)"
        elif pct >= 50:
            return "B (Above Average)"
        elif pct >= 40:
            return "C (Pass)"
        else:
            return "F (Fail)"

    # ---------------------------------------------------------
    # SQL Query APIs (Returning Pandas DataFrames)
    # ---------------------------------------------------------

    def get_all_students_summary_df(self) -> pd.DataFrame:
        """Executes a SQL JOIN query returning consolidated student results."""
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

    def get_student_marks_df(self, roll_no: str, semester: Optional[str] = None) -> pd.DataFrame:
        """Retrieves subject marks for a student via SQL query."""
        if semester:
            query = """
                SELECT subject AS "Subject", marks AS "Marks", max_marks AS "Max Marks", status AS "Status"
                FROM semester_marks
                WHERE roll_no = ? AND semester = ?
                ORDER BY subject ASC;
            """
            params = (roll_no, semester)
        else:
            query = """
                SELECT semester AS "Semester", subject AS "Subject", marks AS "Marks", max_marks AS "Max Marks", status AS "Status"
                FROM semester_marks
                WHERE roll_no = ?
                ORDER BY semester ASC, subject ASC;
            """
            params = (roll_no,)

        with self.get_connection() as conn:
            return pd.read_sql_query(query, conn, params=params)

    def get_student_supplementary_df(self, roll_no: Optional[str] = None) -> pd.DataFrame:
        """Retrieves makeup and backup exam records from SQLite."""
        if roll_no:
            query = """
                SELECT exam_type AS "Exam", semester AS "Semester", subject AS "Subject", 
                       original_marks AS "Original Marks", attempt_marks AS "Attempt Marks", 
                       backup_marks AS "Backup Marks", status AS "Status"
                FROM supplementary_exams
                WHERE roll_no = ?
                ORDER BY id ASC;
            """
            params = (roll_no,)
        else:
            query = """
                SELECT se.roll_no AS "Roll No", s.name AS "Name", se.exam_type AS "Exam", 
                       se.semester AS "Semester", se.subject AS "Subject", 
                       se.original_marks AS "Original Marks", se.attempt_marks AS "Attempt Marks", 
                       se.backup_marks AS "Backup Marks", se.status AS "Status"
                FROM supplementary_exams se
                JOIN students s ON se.roll_no = s.roll_no
                ORDER BY se.id ASC;
            """
            params = ()

        with self.get_connection() as conn:
            return pd.read_sql_query(query, conn, params=params)

    def get_subject_analytics_df(self, semester: str) -> pd.DataFrame:
        """Uses SQL Aggregations (AVG, MIN, MAX, COUNT) to analyze subject difficulty."""
        query = """
            SELECT 
                subject AS "Subject",
                ROUND(AVG(marks), 2) AS "Average Marks",
                MAX(marks) AS "Highest Marks",
                MIN(marks) AS "Lowest Marks",
                SUM(CASE WHEN marks >= 40 THEN 1 ELSE 0 END) AS "Pass Count",
                COUNT(*) AS "Total Appeared",
                ROUND((SUM(CASE WHEN marks >= 40 THEN 1.0 ELSE 0.0 END) / COUNT(*)) * 100.0, 1) AS "Pass Rate (%)"
            FROM semester_marks
            WHERE semester = ?
            GROUP BY subject
            ORDER BY "Pass Rate (%)" DESC;
        """
        with self.get_connection() as conn:
            return pd.read_sql_query(query, conn, params=(semester,))

    def execute_custom_sql(self, sql_query: str) -> Tuple[bool, Optional[pd.DataFrame], str]:
        """
        Executes a custom SQL query provided by the user.
        Safely restricted to SELECT statements for analytical read safety.
        """
        trimmed = sql_query.strip()
        if not trimmed.lower().startswith("select"):
            return False, None, "Security Restriction: Only SELECT queries are permitted in the interactive console."

        try:
            with self.get_connection() as conn:
                df = pd.read_sql_query(trimmed, conn)
                return True, df, f"Query executed successfully. ({len(df)} rows returned)"
        except Exception as e:
            return False, None, f"SQL Error: {str(e)}"

    def add_student_record(self, roll_no: str, name: str, dept: str, gender: str) -> Tuple[bool, str]:
        """Inserts a new student into the database."""
        try:
            with self.get_connection() as conn:
                conn.execute("""
                    INSERT INTO students (roll_no, name, department, gender)
                    VALUES (?, ?, ?, ?);
                """, (roll_no.strip(), name.strip(), dept.strip(), gender.strip()))
                conn.commit()
            return True, f"Student {name} ({roll_no}) added successfully."
        except sqlite3.IntegrityError:
            return False, f"Roll Number {roll_no} already exists in the database."
        except Exception as e:
            return False, str(e)
