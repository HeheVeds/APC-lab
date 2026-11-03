"""
Report Generator Utility Module
Produces formatted student report cards and cohort performance summaries
exportable as text, markdown, or CSV.
"""
from datetime import datetime
from typing import Dict, List
import pandas as pd
from models.student import Student


class ReportGenerator:
    """
    Builds clean, printable academic reports for individual students and entire batches.
    """

    @classmethod
    def generate_student_report_card(cls, student: Student) -> str:
        """Generates an ASCII/Text transcript report card for a single student."""
        summary = student.get_academic_summary()
        now_str = datetime.now().strftime("%d-%b-%Y %H:%M")

        report = []
        report.append("=" * 65)
        report.append("          COLLEGE OF ENGINEERING & TECHNOLOGY")
        report.append("         DEPARTMENT OF COMPUTER SCIENCE")
        report.append("            ACADEMIC PERFORMANCE TRANSCRIPT")
        report.append("=" * 65)
        report.append(f"Generated On  : {now_str}")
        report.append(f"Student Name  : {summary['name']}")
        report.append(f"Roll Number   : {summary['roll_no']}")
        report.append(f"Department    : {summary['department']}")
        report.append(f"Gender        : {summary['gender']}")
        report.append("-" * 65)
        
        # Semester-wise marks breakdown
        for sem, marks in student.semester_data.items():
            sem_total = student.calculate_semester_total(sem)
            sem_pct = student.calculate_semester_percentage(sem)
            report.append(f"\n[{sem.upper()}] (Total: {sem_total:.0f}/500 | Percentage: {sem_pct}%)")
            report.append(f"{'Subject Name':<35} {'Marks':<10} {'Status':<10}")
            report.append("-" * 60)
            for sub, mark in marks.items():
                status = "PASS" if mark >= Student.PASSING_MARKS else "FAIL"
                sub_clean = sub.replace('_', ' ')
                report.append(f"{sub_clean:<35} {mark:<10.1f} {status:<10}")

        # Supplementary exam history
        if student.supplementary_records:
            report.append("\n" + "-" * 65)
            report.append("SUPPLEMENTARY / REMEDIAL EXAM HISTORY:")
            report.append(f"{'Exam':<15} {'Semester':<12} {'Subject':<20} {'Attempt Marks':<15} {'Status'}")
            report.append("-" * 65)
            for rec in student.supplementary_records:
                report.append(
                    f"{rec['Exam_Type']:<15} {rec['Semester']:<12} {rec['Subject']:<20} "
                    f"{rec['Attempt_Marks']:<15.1f} {rec['Status']}"
                )

        # Final Summary
        report.append("\n" + "=" * 65)
        report.append(f"CUMULATIVE PERCENTAGE : {summary['overall_percentage']}%")
        report.append(f"FINAL GRADE           : {summary['overall_grade']}")
        report.append(f"ACADEMIC STATUS       : {summary['status']}")
        if summary['backlogs']:
            report.append(f"ACTIVE BACKLOGS       : {', '.join(summary['backlogs'])}")
        else:
            report.append("ACTIVE BACKLOGS       : NIL (All Clear)")
        report.append("=" * 65)

        return "\n".join(report)

    @classmethod
    def generate_class_summary_report(cls, stats: Dict, toppers_df: pd.DataFrame) -> str:
        """Generates a high-level performance summary for department faculty."""
        now_str = datetime.now().strftime("%d-%b-%Y %H:%M")
        lines = []
        lines.append("=" * 65)
        lines.append("        DEPARTMENT OF COMPUTER SCIENCE - BATCH SUMMARY")
        lines.append("=" * 65)
        lines.append(f"Generated On          : {now_str}")
        lines.append(f"Total Students        : {stats.get('Total Students', 'N/A')}")
        lines.append(f"Class Average         : {stats.get('Class Average (%)', 'N/A')}%")
        lines.append(f"Highest Score         : {stats.get('Highest Score (%)', 'N/A')}%")
        lines.append(f"Lowest Score          : {stats.get('Lowest Score (%)', 'N/A')}%")
        lines.append(f"Median Score          : {stats.get('Median Score (%)', 'N/A')}%")
        lines.append(f"Standard Deviation    : {stats.get('Standard Deviation', 'N/A')}")
        lines.append(f"Overall Pass Rate     : {stats.get('Overall Pass Rate (%)', 'N/A')}%")
        lines.append("-" * 65)
        lines.append("TOP 5 PERFORMERS:")
        lines.append(f"{'Rank':<6} {'Roll No':<12} {'Name':<22} {'Cumulative %':<15} {'Grade'}")
        lines.append("-" * 65)
        for idx, row in toppers_df.iterrows():
            lines.append(f"#{idx+1:<5} {row['Roll No']:<12} {row['Name']:<22} {row['Cumulative %']:<15}% {row['Grade']}")
        lines.append("=" * 65)
        return "\n".join(lines)
