# 🎓 Student Result & Performance Analyzer

An end-to-end Python academic software system built using **Django Web Framework, Tkinter Desktop GUI, Pandas, NumPy, Matplotlib, OOP, Regex, and Exception Handling** to analyze and compare student academic records across multiple semesters, makeup exams, and backup exams.

---

## 🎯 Syllabus Alignment

| Syllabus Requirement | How It Is Implemented |
| :--- | :--- |
| **Unit 1: Python Basics, Lists, Sets, Dictionaries** | Dictionaries for subject marks, lists for backlogs, tuples for rankings. |
| **Unit 2: File Handling & Exception Handling** | Reading CSV files across directories, writing text report cards, catching file errors. |
| **Unit 3: OOP, Inheritance, Polymorphism** | `Person` base class $\rightarrow$ `Student` child class with method overriding. |
| **Unit 3: Python Libraries (NumPy, Pandas, Matplotlib, Regex)** | Array statistics with NumPy, tabular joins with Pandas, graphs with Matplotlib, Roll No validation with `re`. |
| **Unit 4 (Practical 11): GUI using Tkinter** | Standalone desktop GUI (`tkinter_app.py`) with search, filter, and popup marksheets. |
| **Unit 4 (Practical 12): Django Web Application** | Django local server (`manage.py runserver`) with user login & regex validation. |

---

## 🚀 Key Modules & Functions

1. **Import Data Module:**
   - Pre-loaded datasets for Semester 1, 2, 3, Makeup, and Backup exams (15 Computer Science students with Marathi names).
   - Robust file handling and regex validation for Roll Numbers (`ResultValidator`).

2. **Performance Analysis Engine:**
   - Total marks, semester percentage, cumulative percentage, and standard grades ($O, A+, A, B+, B, C, F$).
   - Active backlog detector (identifying subjects $< 40$ marks).

3. **Multi-Semester Comparison Module:**
   - Progression tracking across Semester 1 $\rightarrow$ Semester 2 $\rightarrow$ Semester 3.
   - Growth / Dip analysis ($\Delta\%$ growth/dip metrics).

4. **Makeup & Backup Exam Analysis:**
   - Tracks students who took supplementary (Makeup) and second re-sit (Backup) exams.
   - Shows improvement deltas and confirms final backlog clearance.

5. **Student Ranking & Cohort Statistics:**
   - Identifies Top 5 Toppers and Bottom 5 students requiring remedial support.
   - Computes Class Average, Median, Standard Deviation, and Batch Pass Rate.

6. **Subject-Wise Curriculum Analysis:**
   - Evaluates subject difficulty, pass percentages, and average scores per semester.

7. **Report Generation & Export:**
   - Formatted single-student Academic Transcript Cards (`.txt`).
   - Executive Batch Summary reports for faculty meetings (`.txt`).

---

## 🛠️ Project Structure

```text
Student_Result_Analyzer/
├── ⚡ run_django.bat          # 1-Click launcher for Django Web Server
├── ⚡ run_tkinter.bat         # 1-Click launcher for Tkinter Desktop GUI
├── 🐍 manage.py               # Django administrative utility
├── 🐍 tkinter_app.py          # Tkinter Desktop GUI (Practical 11)
├── 📋 requirements.txt        # Python dependencies (Django, Pandas, NumPy, etc.)
├── 📖 README.md               # Project documentation
├── 📂 django_project/         # Django Project configuration
│   ├── settings.py           # Django settings
│   ├── urls.py               # URL routing
│   └── wsgi.py
├── 📂 analyzer_app/           # Django Application (Practical 12)
│   ├── forms.py              # AdminLoginForm with Django RegexValidator
│   ├── views.py              # Pure Python login & dashboard views
│   └── urls.py
├── 📂 data/                   # Academic Datasets (CSV & SQLite)
│   ├── semester_1.csv         # Sem 1 scores (15 Computer Science students)
│   ├── semester_2.csv         # Sem 2 scores
│   ├── semester_3.csv         # Sem 3 scores
│   ├── makeup_exam.csv        # Supplementary sitting results
│   ├── backup_exam.csv        # Re-sit sitting results
│   └── student_records.db     # SQLite Relational Database
├── 📂 models/                 # OOP Architecture
│   ├── student.py             # OOP Person and Student classes
│   └── analyzer.py            # ResultAnalyzer (Pandas/NumPy data processing)
└── 📂 utils/                  # Helpers
    ├── validator.py           # Regex validators & custom exceptions
    └── report_generator.py    # Transcript and class summary generator
```

---

## 🏃 How to Run

### 1. Django Web Application (Practical 12)
* **1-Click:** Double-click **`run_django.bat`** on your Desktop.
* **Terminal:**
  ```powershell
  python manage.py runserver
  ```
* Open in browser: **`http://127.0.0.1:8000/`**
* **Login Credentials:** Username: `admin` | Password: `admin123`

### 2. Tkinter Desktop GUI (Practical 11)
* **1-Click:** Double-click **`run_tkinter.bat`** on your Desktop.
* **Terminal:**
  ```powershell
  python tkinter_app.py
  ```
* **Login Credentials:** Username: `admin` | Password: `admin123`
