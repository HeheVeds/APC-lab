"""
Result Analyzer Module
Core analytical engine utilizing Pandas, NumPy, and OOP Student entities
to calculate metrics, perform cross-semester tracking, and generate visualizations.
"""
import os
from typing import Dict, List, Optional, Tuple
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from models.student import Student
from utils.validator import ResultValidator, MissingColumnError, DataValidationError
from database.db_manager import DatabaseManager


class ResultAnalyzer:
    """
    Manages datasets for Semester 1, 2, 3, Makeup, and Backup exams.
    Performs data cleaning, student aggregation, ranking, and statistical calculations.
    """

    def __init__(self, db_path: Optional[str] = None):
        self.sem1_df: Optional[pd.DataFrame] = None
        self.sem2_df: Optional[pd.DataFrame] = None
        self.sem3_df: Optional[pd.DataFrame] = None
        self.makeup_df: Optional[pd.DataFrame] = None
        self.backup_df: Optional[pd.DataFrame] = None
        self.students: Dict[str, Student] = {}
        self.data_loaded: bool = False
        self.db: DatabaseManager = DatabaseManager(db_path)

    def load_data(
        self,
        sem1_path_or_buf,
        sem2_path_or_buf,
        sem3_path_or_buf,
        makeup_path_or_buf=None,
        backup_path_or_buf=None
    ) -> Dict[str, str]:
        """
        Loads CSV or Excel data sources into DataFrames and populates Student models.
        Includes robust exception handling and validation.
        """
        logs = {}
        try:
            # Helper to read CSV or DataFrame/buffer
            def _read_data(source):
                if source is None:
                    return None
                if isinstance(source, pd.DataFrame):
                    return source.copy()
                if isinstance(source, str):
                    if not os.path.exists(source):
                        raise FileNotFoundError(f"File not found: {source}")
                    if source.endswith(('.xlsx', '.xls')):
                        return pd.read_excel(source)
                    return pd.read_csv(source)
                # Streamlit UploadedFile or file-like buffer
                if hasattr(source, 'name') and source.name.endswith(('.xlsx', '.xls')):
                    return pd.read_excel(source)
                return pd.read_csv(source)

            self.sem1_df = _read_data(sem1_path_or_buf)
            self.sem2_df = _read_data(sem2_path_or_buf)
            self.sem3_df = _read_data(sem3_path_or_buf)
            self.makeup_df = _read_data(makeup_path_or_buf) if makeup_path_or_buf is not None else None
            self.backup_df = _read_data(backup_path_or_buf) if backup_path_or_buf is not None else None

            # Validate column presence in base semester files
            mandatory = ["Roll_No", "Name"]
            for sem_name, df in [("Semester 1", self.sem1_df), ("Semester 2", self.sem2_df), ("Semester 3", self.sem3_df)]:
                if df is not None:
                    valid, missing = ResultValidator.validate_dataset_columns(df.columns.tolist(), mandatory)
                    if not valid:
                        raise MissingColumnError(f"{sem_name} missing required columns: {', '.join(missing)}")

            self._build_student_registry()

            # Sync to SQLite relational database
            if isinstance(sem1_path_or_buf, str) and isinstance(sem2_path_or_buf, str) and isinstance(sem3_path_or_buf, str):
                self.db.sync_from_csv_files(
                    sem1_path_or_buf,
                    sem2_path_or_buf,
                    sem3_path_or_buf,
                    makeup_path_or_buf if isinstance(makeup_path_or_buf, str) else None,
                    backup_path_or_buf if isinstance(backup_path_or_buf, str) else None
                )

            self.data_loaded = True
            logs["status"] = "Success"
            logs["message"] = f"Successfully loaded records for {len(self.students)} students."
            return logs

        except Exception as e:
            self.data_loaded = False
            logs["status"] = "Error"
            logs["message"] = str(e)
            return logs

    def _build_student_registry(self) -> None:
        """Constructs Student objects and parses marks across semesters."""
        self.students = {}
        non_subject_cols = {"Roll_No", "Name", "Department", "Gender"}

        # Helper to process a semester DataFrame
        def _process_sem(df: pd.DataFrame, sem_label: str):
            if df is None:
                return
            subject_cols = [c for c in df.columns if c not in non_subject_cols]
            for _, row in df.iterrows():
                roll = str(row["Roll_No"]).strip()
                name = str(row["Name"]).strip()
                dept = str(row.get("Department", "Computer Science")).strip()
                gender = str(row.get("Gender", "Unspecified")).strip()

                if roll not in self.students:
                    self.students[roll] = Student(roll_no=roll, name=name, department=dept, gender=gender)

                marks = {sub: float(row[sub]) for sub in subject_cols if pd.notnull(row[sub])}
                self.students[roll].add_semester_marks(sem_label, marks)

        _process_sem(self.sem1_df, "Semester 1")
        _process_sem(self.sem2_df, "Semester 2")
        _process_sem(self.sem3_df, "Semester 3")

        # Process Makeup Exam records
        if self.makeup_df is not None:
            for _, row in self.makeup_df.iterrows():
                roll = str(row["Roll_No"]).strip()
                if roll in self.students:
                    record = {
                        "Exam_Type": "Makeup Exam",
                        "Semester": str(row.get("Semester", "Unknown")),
                        "Subject": str(row.get("Subject", "Unknown")),
                        "Original_Marks": float(row.get("Original_Marks", 0)),
                        "Attempt_Marks": float(row.get("Makeup_Marks", 0)),
                        "Status": str(row.get("Status", "Unknown"))
                    }
                    self.students[roll].add_supplementary_record(record)

        # Process Backup Exam records
        if self.backup_df is not None:
            for _, row in self.backup_df.iterrows():
                roll = str(row["Roll_No"]).strip()
                if roll in self.students:
                    record = {
                        "Exam_Type": "Backup Exam",
                        "Semester": str(row.get("Semester", "Unknown")),
                        "Subject": str(row.get("Subject", "Unknown")),
                        "Original_Marks": float(row.get("Original_Marks", 0)),
                        "Makeup_Marks": float(row.get("Makeup_Marks", 0)),
                        "Attempt_Marks": float(row.get("Backup_Marks", 0)),
                        "Status": str(row.get("Status", "Unknown"))
                    }
                    self.students[roll].add_supplementary_record(record)

    def get_all_students_df(self) -> pd.DataFrame:
        """Returns consolidated DataFrame of all students with cumulative performance."""
        data = []
        for s in self.students.values():
            summary = s.get_academic_summary()
            row = {
                "Roll No": summary["roll_no"],
                "Name": summary["name"],
                "Department": summary["department"],
                "Gender": summary["gender"],
                "Sem 1 %": summary["sem_percentages"].get("Semester 1", np.nan),
                "Sem 2 %": summary["sem_percentages"].get("Semester 2", np.nan),
                "Sem 3 %": summary["sem_percentages"].get("Semester 3", np.nan),
                "Cumulative %": summary["overall_percentage"],
                "Grade": summary["overall_grade"],
                "Status": summary["status"],
                "Active Backlogs": len(summary["backlogs"])
            }
            data.append(row)
        return pd.DataFrame(data).sort_values(by="Roll No")

    def get_rankings(self) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """Returns Top 5 and Bottom 5 performers based on cumulative percentage."""
        df = self.get_all_students_df()
        top_5 = df.nlargest(5, "Cumulative %")[["Roll No", "Name", "Department", "Cumulative %", "Grade", "Status"]].reset_index(drop=True)
        bottom_5 = df.nsmallest(5, "Cumulative %")[["Roll No", "Name", "Department", "Cumulative %", "Grade", "Status"]].reset_index(drop=True)
        return top_5, bottom_5

    def get_class_statistics(self) -> Dict:
        """
        Computes statistical metrics using NumPy Array operations
        (Syllabus Unit 1 Arrays, Unit 3 & Practical 9: NumPy Array Operations).
        """
        df = self.get_all_students_df()
        if df.empty:
            return {}
        
        # NumPy Array Operations 
        pct_array = np.array(df["Cumulative %"].dropna().values, dtype=float)
        passed_count = (df["Status"] == "PASS").sum()
        total_count = len(df)

        # Lambda Function demonstration (Unit 1, Practical 5)
        calc_stat = lambda arr, func: round(float(func(arr)), 2) if len(arr) > 0 else 0.0

        return {
            "Total Students": total_count,
            "Class Average (%)": calc_stat(pct_array, np.mean),
            "Highest Score (%)": calc_stat(pct_array, np.max),
            "Lowest Score (%)": calc_stat(pct_array, np.min),
            "Median Score (%)": calc_stat(pct_array, np.median),
            "Standard Deviation": calc_stat(pct_array, np.std),
            "Overall Pass Rate (%)": round((passed_count / total_count) * 100.0, 2) if total_count > 0 else 0.0
        }

    def get_subject_statistics(self, semester_name: str) -> pd.DataFrame:
        """Returns average, minimum, maximum, and pass percentage per subject for a semester."""
        df_map = {
            "Semester 1": self.sem1_df,
            "Semester 2": self.sem2_df,
            "Semester 3": self.sem3_df
        }
        df = df_map.get(semester_name)
        if df is None:
            return pd.DataFrame()

        non_sub = {"Roll_No", "Name", "Department", "Gender"}
        subject_cols = [c for c in df.columns if c not in non_sub]

        stats = []
        for sub in subject_cols:
            scores = pd.to_numeric(df[sub], errors='coerce').dropna()
            total = len(scores)
            passed = (scores >= Student.PASSING_MARKS).sum()
            stats.append({
                "Subject": sub.replace('_', ' '),
                "Average Marks": round(scores.mean(), 2),
                "Highest Marks": scores.max(),
                "Lowest Marks": scores.min(),
                "Pass Count": passed,
                "Pass Rate (%)": round((passed / total) * 100.0, 2) if total > 0 else 0.0
            })
        return pd.DataFrame(stats).sort_values(by="Pass Rate (%)", ascending=False)

    def get_student_trajectory(self, roll_no: str) -> Optional[Dict]:
        """Retrieves performance metrics across Semesters 1, 2, and 3 for a given student."""
        student = self.students.get(roll_no.strip())
        if not student:
            return None
        
        sem1_pct = student.calculate_semester_percentage("Semester 1")
        sem2_pct = student.calculate_semester_percentage("Semester 2")
        sem3_pct = student.calculate_semester_percentage("Semester 3")
        
        # Calculate delta changes
        delta_1_2 = round(sem2_pct - sem1_pct, 2) if sem1_pct > 0 and sem2_pct > 0 else None
        delta_2_3 = round(sem3_pct - sem2_pct, 2) if sem2_pct > 0 and sem3_pct > 0 else None
        
        return {
            "student": student,
            "sem1_pct": sem1_pct,
            "sem2_pct": sem2_pct,
            "sem3_pct": sem3_pct,
            "delta_1_2": delta_1_2,
            "delta_2_3": delta_2_3,
            "trajectory": [sem1_pct, sem2_pct, sem3_pct]
        }

    # Visualizations using Matplotlib
    def plot_student_semester_trend(self, roll_no: str):
        """Generates a line plot showing student's percentage trajectory across Sem 1, 2, 3."""
        traj = self.get_student_trajectory(roll_no)
        if not traj:
            return None

        fig, ax = plt.subplots(figsize=(7, 3.8))
        semesters = ["Semester 1", "Semester 2", "Semester 3"]
        scores = traj["trajectory"]

        ax.plot(semesters, scores, marker='o', linewidth=2.5, markersize=8, color='#1E88E5', label="Student %")
        
        # Reference threshold line (40%)
        ax.axhline(40, color='#E53935', linestyle='--', alpha=0.7, label="Passing Cutoff (40%)")

        for i, txt in enumerate(scores):
            ax.annotate(f"{txt}%", (semesters[i], scores[i] + 1.5), ha='center', fontweight='bold', fontsize=10)

        ax.set_ylim(0, 110)
        ax.set_title(f"Semester Progression Trend: {traj['student'].name} ({roll_no})", fontsize=12, pad=12)
        ax.set_ylabel("Percentage (%)", fontsize=10)
        ax.grid(True, linestyle=':', alpha=0.6)
        ax.legend(loc='lower right')
        plt.tight_layout()
        return fig

    def plot_student_subject_marks(self, roll_no: str, semester_name: str):
        """Generates a bar chart of marks for a specific student and semester."""
        student = self.students.get(roll_no)
        if not student:
            return None
        subjects = student.get_subjects(semester_name)
        if not subjects:
            return None

        fig, ax = plt.subplots(figsize=(8, 4))
        names = [s.replace('_', ' ') for s in subjects.keys()]
        marks = list(subjects.values())
        colors = ['#43A047' if m >= 40 else '#E53935' for m in marks]

        bars = ax.bar(names, marks, color=colors, width=0.55, edgecolor='black', linewidth=0.8)
        ax.axhline(40, color='#E53935', linestyle='--', linewidth=1.2, label="Pass Mark (40)")

        for bar in bars:
            height = bar.get_height()
            ax.annotate(f'{height:.0f}',
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),  
                        textcoords="offset points",
                        ha='center', va='bottom', fontweight='bold')

        ax.set_ylim(0, 115)
        ax.set_ylabel("Marks Obtained (Max: 100)")
        ax.set_title(f"{semester_name} Subject Scores - {student.name}", fontsize=12, pad=10)
        ax.legend()
        plt.xticks(rotation=20, ha='right')
        plt.tight_layout()
        return fig

    def plot_grade_distribution(self):
        """Generates a donut chart displaying cohort grade distribution."""
        df = self.get_all_students_df()
        if df.empty:
            return None
        grade_counts = df["Grade"].value_counts()

        fig, ax = plt.subplots(figsize=(6, 5))
        wedges, texts, autotexts = ax.pie(
            grade_counts.values,
            labels=grade_counts.index,
            autopct='%1.1f%%',
            startangle=140,
            wedgeprops=dict(width=0.45, edgecolor='white', linewidth=2)
        )
        for autotext in autotexts:
            autotext.set_fontweight('bold')

        ax.set_title("Overall Grade Distribution (Cohort)", fontsize=13, pad=15)
        plt.tight_layout()
        return fig
