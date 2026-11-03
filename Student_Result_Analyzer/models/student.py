"""
Student Model (Object-Oriented Programming)
Encapsulates individual student academic data, calculation of percentages, grades, and backlog tracking.
"""
from typing import Dict, List, Optional


class Person:
    """
    Base Class representing a human entity.
    Demonstrates OOP Inheritance, Constructors, Destructors, and Polymorphism
    (Syllabus Unit 3, Practicals 7 & 8).
    """
    def __init__(self, name: str, gender: str = "Unspecified"):
        self.name: str = name.strip()
        self.gender: str = gender.strip()

    def get_details(self) -> str:
        """Base method meant to be overridden in child classes (Polymorphism)."""
        return f"{self.name} ({self.gender})"

    def __del__(self):
        """Destructor method demonstrating object cleanup lifecycle (Practical 7)."""
        pass


class Student(Person):
    """
    Child class inheriting from Person (OOP Inheritance).
    Represents an individual student with their semester scores,
    makeup/backup exam records, and academic status.
    """
    PASSING_MARKS = 40.0

    def __init__(self, roll_no: str, name: str, department: str = "Computer Science", gender: str = "Unspecified"):
        # Constructor 
        super().__init__(name=name, gender=gender)
        self.roll_no: str = roll_no.strip()
        self.department: str = department.strip()
        
        # semester_data: { 'Semester 1': {'Mathematics_1': 88, 'Physics': 85, ...}, ... }
        self.semester_data: Dict[str, Dict[str, float]] = {}
        
        # supplementary_records: list of dictionaries tracking makeup/backup attempts
        self.supplementary_records: List[Dict] = []

    def get_details(self) -> str:
        """
        Polymorphic Method Overriding:
        Overrides Person.get_details() to provide student-specific identifiers.
        """
        return f"Roll: {self.roll_no} | {self.name} | Dept: {self.department}"

    def add_semester_marks(self, semester_name: str, marks_dict: Dict[str, float]) -> None:
        """Stores subject marks for a given semester."""
        cleaned_marks = {k: float(v) for k, v in marks_dict.items() if str(v).replace('.', '', 1).isdigit()}
        self.semester_data[semester_name] = cleaned_marks

    def add_supplementary_record(self, record: Dict) -> None:
        """Appends supplementary attempt (Makeup / Backup)."""
        self.supplementary_records.append(record)

    def get_subjects(self, semester_name: str) -> Dict[str, float]:
        """Returns subject-wise marks for a specific semester."""
        return self.semester_data.get(semester_name, {})

    def calculate_semester_total(self, semester_name: str) -> float:
        """Calculates total marks obtained in a semester."""
        subjects = self.get_subjects(semester_name)
        return sum(subjects.values()) if subjects else 0.0

    def calculate_semester_percentage(self, semester_name: str) -> float:
        """Calculates percentage obtained in a semester (assumes 100 max marks per subject)."""
        subjects = self.get_subjects(semester_name)
        if not subjects:
            return 0.0
        total = sum(subjects.values())
        max_marks = len(subjects) * 100.0
        return round((total / max_marks) * 100.0, 2)

    def calculate_overall_percentage(self) -> float:
        """Calculates cumulative percentage across all registered semesters."""
        total_marks = 0.0
        total_subjects = 0
        for sem, subs in self.semester_data.items():
            total_marks += sum(subs.values())
            total_subjects += len(subs)
        if total_subjects == 0:
            return 0.0
        return round((total_marks / (total_subjects * 100.0)) * 100.0, 2)

    @staticmethod
    def calculate_grade(percentage: float) -> str:
        """Maps percentage to standard letter grade."""
        if percentage >= 90:
            return "O (Outstanding)"
        elif percentage >= 80:
            return "A+ (Excellent)"
        elif percentage >= 70:
            return "A (Very Good)"
        elif percentage >= 60:
            return "B+ (Good)"
        elif percentage >= 50:
            return "B (Above Average)"
        elif percentage >= 40:
            return "C (Pass)"
        else:
            return "F (Fail)"

    def get_failed_subjects(self, semester_name: Optional[str] = None) -> List[str]:
        """Returns list of subjects with marks below passing threshold."""
        failed = []
        if semester_name:
            subs = self.get_subjects(semester_name)
            for sub, mark in subs.items():
                if mark < self.PASSING_MARKS:
                    failed.append(f"{sub} ({mark})")
        else:
            for sem, subs in self.semester_data.items():
                for sub, mark in subs.items():
                    if mark < self.PASSING_MARKS:
                        failed.append(f"{sem}: {sub} ({mark})")
        return failed

    def has_backlogs(self) -> bool:
        """Checks if student has any active failed subject."""
        return len(self.get_failed_subjects()) > 0

    def get_academic_summary(self) -> Dict:
        """Returns a comprehensive summary dictionary for reports and UI cards."""
        overall_pct = self.calculate_overall_percentage()
        failed_subs = self.get_failed_subjects()
        sem_percentages = {sem: self.calculate_semester_percentage(sem) for sem in self.semester_data}
        
        return {
            "roll_no": self.roll_no,
            "name": self.name,
            "department": self.department,
            "gender": self.gender,
            "semesters_completed": len(self.semester_data),
            "sem_percentages": sem_percentages,
            "overall_percentage": overall_pct,
            "overall_grade": self.calculate_grade(overall_pct),
            "status": "PASS" if not failed_subs else "ATKT / BACKLOG",
            "backlogs": failed_subs,
            "supplementary_attempts": len(self.supplementary_records)
        }
