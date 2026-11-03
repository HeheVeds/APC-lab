"""
Tkinter Desktop GUI for Student Result & Performance Analyzer
Includes Admin Authentication Login Screen and Interactive Analytics Dashboard
(Syllabus Unit 4, Practical 11: Implementation of GUI using Tkinter).
"""
import os
import sys
import tkinter as tk
from tkinter import ttk, messagebox

# Ensure root directory is in sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from models.analyzer import ResultAnalyzer
from utils.validator import ResultValidator


class StudentAnalyzerTkinterApp:
    """Tkinter Desktop Application featuring Admin Login and Academic Dashboard."""

    # Pre-configured Admin Credentials
    ADMIN_USERNAME = "admin"
    ADMIN_PASSWORD = "Admin@123"

    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Analyzer - Admin Portal")
        self.root.geometry("940x600")
        self.root.minsize(840, 520)
        self.root.configure(bg="#F3F4F6")

        # Initialize Analytical Engine
        self.analyzer = ResultAnalyzer()
        base_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(base_dir, "data")
        self.analyzer.load_data(
            os.path.join(data_dir, "semester_1.csv"),
            os.path.join(data_dir, "semester_2.csv"),
            os.path.join(data_dir, "semester_3.csv"),
            os.path.join(data_dir, "makeup_exam.csv"),
            os.path.join(data_dir, "backup_exam.csv")
        )

        self.current_frame = None
        self.show_login_page()

    def _clear_current_frame(self):
        """Removes the active frame from the root window."""
        if self.current_frame is not None:
            self.current_frame.destroy()
            self.current_frame = None

    # =========================================================================
    # PAGE 1: ADMIN LOGIN PAGE
    # =========================================================================
    def show_login_page(self):
        """Displays a clean, professional Admin Authentication screen."""
        self._clear_current_frame()
        self.root.title("Admin Login - Student Result & Performance Analyzer")

        self.current_frame = tk.Frame(self.root, bg="#F3F4F6")
        self.current_frame.pack(fill=tk.BOTH, expand=True)

        # Centered Login Card
        card = tk.Frame(self.current_frame, bg="white", padx=35, pady=30, relief=tk.RAISED, bd=1)
        card.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Logo / Header
        title_lbl = tk.Label(
            card,
            text="🔐 Admin Portal Login",
            font=("Arial", 18, "bold"),
            fg="#1E3A8A",
            bg="white"
        )
        title_lbl.pack(pady=(0, 4))

        subtitle_lbl = tk.Label(
            card,
            text="Student Academic Performance & Result Analyzer",
            font=("Arial", 9),
            fg="#6B7280",
            bg="white"
        )
        subtitle_lbl.pack(pady=(0, 20))

        # Username Field
        user_lbl = tk.Label(card, text="Admin Username:", font=("Arial", 10, "bold"), fg="#374151", bg="white", anchor="w")
        user_lbl.pack(fill=tk.X, pady=(5, 2))
        
        self.username_entry = tk.Entry(card, font=("Arial", 11), width=30, bd=1, relief=tk.SOLID)
        self.username_entry.pack(pady=(0, 12), ipady=4)
        self.username_entry.insert(0, "admin")  # Convenient default
        self.username_entry.focus_set()

        # Password Field
        pass_lbl = tk.Label(card, text="Password:", font=("Arial", 10, "bold"), fg="#374151", bg="white", anchor="w")
        pass_lbl.pack(fill=tk.X, pady=(5, 2))

        self.password_entry = tk.Entry(card, font=("Arial", 11), width=30, bd=1, relief=tk.SOLID, show="*")
        self.password_entry.pack(pady=(0, 8), ipady=4)
        self.password_entry.insert(0, "Admin@123")  # Convenient default

        # Show Password Toggle
        self.show_pass_var = tk.BooleanVar(value=False)
        show_pass_cb = tk.Checkbutton(
            card,
            text="Show Password",
            variable=self.show_pass_var,
            command=self._toggle_password_visibility,
            bg="white",
            fg="#4B5563",
            font=("Arial", 9)
        )
        show_pass_cb.pack(anchor="w", pady=(0, 15))

        # Login Action Button
        login_btn = tk.Button(
            card,
            text="🚀 Log In to Dashboard",
            font=("Arial", 11, "bold"),
            bg="#1E3A8A",
            fg="white",
            activebackground="#1E40AF",
            activeforeground="white",
            relief=tk.FLAT,
            cursor="hand2",
            padx=15,
            pady=6,
            command=self._handle_login
        )
        login_btn.pack(fill=tk.X, pady=(5, 10))

        # Quick Hint
        hint_lbl = tk.Label(
            card,
            text="Default Credentials:\nUsername: admin  |  Password: Admin@123",
            font=("Arial", 8, "italic"),
            fg="#9CA3AF",
            bg="white"
        )
        hint_lbl.pack(pady=(5, 0))

        # Bind Enter key to login
        self.root.bind("<Return>", lambda event: self._handle_login())

    def _toggle_password_visibility(self):
        """Toggles the password field between hidden and visible."""
        if self.show_pass_var.get():
            self.password_entry.configure(show="")
        else:
            self.password_entry.configure(show="*")

    def _handle_login(self):
        """Validates credentials using regex rules and navigates to the dashboard."""
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        # 1. Regular Expression (Regex) Validation (Syllabus Unit 3 & 4)
        is_valid, validation_err = ResultValidator.validate_login_form(username, password)
        if not is_valid:
            messagebox.showwarning("Validation Error", f"Input Validation Failed:\n\n{validation_err}")
            return

        # 2. Credential Verification
        if username == self.ADMIN_USERNAME and password == self.ADMIN_PASSWORD:
            self.root.unbind("<Return>")
            messagebox.showinfo("Login Successful", f"Welcome back, Administrator ({username})!")
            self.show_dashboard_page()
        else:
            messagebox.showerror("Access Denied", "Authentication Failed:\nInvalid Admin Username or Password.\n\nHint: admin / Admin@123")
            self.password_entry.delete(0, tk.END)
            self.password_entry.focus_set()

    # =========================================================================
    # PAGE 2: MAIN ANALYZER DASHBOARD
    # =========================================================================
    def show_dashboard_page(self):
        """Displays the Student Result & Performance Analyzer Dashboard."""
        self._clear_current_frame()
        self.root.title("Student Result & Performance Analyzer - Admin Dashboard")

        self.current_frame = tk.Frame(self.root, bg="#F3F4F6")
        self.current_frame.pack(fill=tk.BOTH, expand=True)

        # Header Bar with Logout button
        header_frame = tk.Frame(self.current_frame, bg="#1E3A8A", height=60)
        header_frame.pack(fill=tk.X)

        title_lbl = tk.Label(
            header_frame,
            text="🎓 Student Result & Performance Analyzer",
            font=("Arial", 15, "bold"),
            fg="white",
            bg="#1E3A8A"
        )
        title_lbl.pack(side=tk.LEFT, padx=15, pady=12)

        # Admin Badge & Logout
        admin_box = tk.Frame(header_frame, bg="#1E3A8A")
        admin_box.pack(side=tk.RIGHT, padx=15, pady=10)

        admin_badge = tk.Label(
            admin_box,
            text="👤 Admin: admin",
            font=("Arial", 10),
            fg="#93C5FD",
            bg="#1E3A8A"
        )
        admin_badge.pack(side=tk.LEFT, padx=8)

        logout_btn = tk.Button(
            admin_box,
            text="🚪 Logout",
            font=("Arial", 9, "bold"),
            bg="#DC2626",
            fg="white",
            activebackground="#B91C1C",
            activeforeground="white",
            relief=tk.FLAT,
            cursor="hand2",
            padx=8,
            pady=2,
            command=self._handle_logout
        )
        logout_btn.pack(side=tk.LEFT)

        # Control Panel / Filter & Actions Frame
        control_frame = tk.Frame(self.current_frame, pady=8, padx=12, bg="#FFFFFF", relief=tk.SOLID, bd=1)
        control_frame.pack(fill=tk.X, padx=10, pady=(8, 4))

        tk.Label(control_frame, text="Search Student:", font=("Arial", 10, "bold"), bg="#FFFFFF").pack(side=tk.LEFT, padx=(5, 3))
        self.search_entry = tk.Entry(control_frame, font=("Arial", 10), width=20)
        self.search_entry.pack(side=tk.LEFT, padx=5)

        search_btn = tk.Button(control_frame, text="🔍 Filter", command=self._filter_data, bg="#3B82F6", fg="white", cursor="hand2")
        search_btn.pack(side=tk.LEFT, padx=3)

        reset_btn = tk.Button(control_frame, text="🔄 Reset", command=self._populate_data, cursor="hand2")
        reset_btn.pack(side=tk.LEFT, padx=3)

        chart_btn = tk.Button(control_frame, text="📊 Grade Chart", command=self._show_grade_chart, bg="#10B981", fg="white", cursor="hand2")
        chart_btn.pack(side=tk.LEFT, padx=5)

        trend_btn = tk.Button(control_frame, text="📈 Student Trend", command=self._show_trend_chart, bg="#8B5CF6", fg="white", cursor="hand2")
        trend_btn.pack(side=tk.LEFT, padx=3)

        # Statistics Indicator Bar
        self.stats_var = tk.StringVar()
        stats_lbl = tk.Label(self.current_frame, textvariable=self.stats_var, font=("Arial", 9, "italic"), fg="#4B5563", bg="#F3F4F6")
        stats_lbl.pack(pady=3)

        # Table Frame (Treeview)
        table_frame = tk.Frame(self.current_frame, padx=10, pady=2, bg="#F3F4F6")
        table_frame.pack(fill=tk.BOTH, expand=True)

        columns = ("Roll No", "Name", "Department", "Sem 1 %", "Sem 2 %", "Sem 3 %", "Cumulative %", "Grade", "Status")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings", selectmode="browse")

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor=tk.CENTER, width=95)
        self.tree.column("Name", width=140, anchor=tk.W)

        # Vertical Scrollbar
        v_scroll = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=v_scroll.set)

        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        v_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.tree.bind("<Double-1>", self._on_student_double_click)

        # Populate data into the table
        self._populate_data()

    def _handle_logout(self):
        """Logs out administrator and returns to login screen."""
        if messagebox.askyesno("Confirm Logout", "Are you sure you want to log out of the Admin Portal?"):
            self.show_login_page()

    def _populate_data(self, df=None):
        """Populates the Treeview with student records."""
        for item in self.tree.get_children():
            self.tree.delete(item)

        if df is None:
            df = self.analyzer.get_all_students_df()

        for _, row in df.iterrows():
            vals = (
                row["Roll No"],
                row["Name"],
                row["Department"],
                f"{row['Sem 1 %']:.1f}%" if str(row['Sem 1 %']) != 'nan' else "-",
                f"{row['Sem 2 %']:.1f}%" if str(row['Sem 2 %']) != 'nan' else "-",
                f"{row['Sem 3 %']:.1f}%" if str(row['Sem 3 %']) != 'nan' else "-",
                f"{row['Cumulative %']:.2f}%",
                row["Grade"],
                row["Status"]
            )
            self.tree.insert("", tk.END, values=vals)

        stats = self.analyzer.get_class_statistics()
        self.stats_var.set(
            f"Total Students: {stats.get('Total Students')} | "
            f"Class Average: {stats.get('Class Average (%)')}% | "
            f"Pass Rate: {stats.get('Overall Pass Rate (%)')}%"
        )

    def _filter_data(self):
        """Filters table by student name or roll number."""
        query = self.search_entry.get().strip().lower()
        if not query:
            self._populate_data()
            return
        df = self.analyzer.get_all_students_df()
        filtered = df[
            df["Roll No"].str.lower().str.contains(query, na=False) |
            df["Name"].str.lower().str.contains(query, na=False)
        ]
        self._populate_data(filtered)

    def _on_student_double_click(self, event):
        """Shows detailed student marksheet on double-click."""
        selected = self.tree.selection()
        if not selected:
            return
        vals = self.tree.item(selected[0], "values")
        roll = vals[0]
        student = self.analyzer.students.get(roll)
        if student:
            summary = student.get_academic_summary()
            details = (
                f"Student: {summary['name']}\n"
                f"Roll No: {summary['roll_no']}\n"
                f"Department: {summary['department']}\n"
                f"Cumulative %: {summary['overall_percentage']}%\n"
                f"Grade: {summary['overall_grade']}\n"
                f"Status: {summary['status']}\n"
                f"Backlogs: {', '.join(summary['backlogs']) if summary['backlogs'] else 'None (All Clear)'}"
            )
            messagebox.showinfo(f"Student Details - {summary['name']}", details)

    def _show_grade_chart(self):
        """Displays grade distribution pie/donut chart in a popup window."""
        import matplotlib.pyplot as plt
        fig = self.analyzer.plot_grade_distribution()
        if fig:
            plt.show()

    def _show_trend_chart(self):
        """Displays semester progression curve for the selected student."""
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Selection Required", "Please select a student from the table first to view their progression trend.")
            return
        vals = self.tree.item(selected[0], "values")
        roll = vals[0]
        import matplotlib.pyplot as plt
        fig = self.analyzer.plot_student_semester_trend(roll)
        if fig:
            plt.show()


def main():
    root = tk.Tk()
    app = StudentAnalyzerTkinterApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
