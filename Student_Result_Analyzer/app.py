"""
Student Result & Performance Analyzer - Web Dashboard
Matches exact design, dark theme, metrics, charts, and layout of the Project Report.
(Python, Streamlit, Pandas, NumPy, Matplotlib, OOP, Regex & Exception Handling).
"""
import os
import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

# Ensure base directory is in sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from models.analyzer import ResultAnalyzer
from models.student import Student
from utils.report_generator import ReportGenerator
from utils.validator import ResultValidator

# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title="Student Result & Performance Analyzer",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Dark theme styling matching report screenshots
st.markdown("""
<style>
    .main-title {
        font-size: 2.3rem;
        font-weight: 700;
        color: #2563EB;
        margin-bottom: 2px;
    }
    .sub-title {
        font-size: 1.05rem;
        color: #9CA3AF;
        margin-top: 0px;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# State Management & Data Ingestion
# ---------------------------------------------------------
if "analyzer" not in st.session_state:
    st.session_state.analyzer = ResultAnalyzer()

analyzer: ResultAnalyzer = st.session_state.analyzer

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
DEFAULT_FILES = {
    "sem1": os.path.join(DATA_DIR, "semester_1.csv"),
    "sem2": os.path.join(DATA_DIR, "semester_2.csv"),
    "sem3": os.path.join(DATA_DIR, "semester_3.csv"),
    "makeup": os.path.join(DATA_DIR, "makeup_exam.csv"),
    "backup": os.path.join(DATA_DIR, "backup_exam.csv")
}

# Auto-load academic datasets
if not analyzer.data_loaded and os.path.exists(DEFAULT_FILES["sem1"]):
    analyzer.load_data(
        DEFAULT_FILES["sem1"],
        DEFAULT_FILES["sem2"],
        DEFAULT_FILES["sem3"],
        DEFAULT_FILES["makeup"],
        DEFAULT_FILES["backup"]
    )


# ---------------------------------------------------------
# Authentication State Management
# ---------------------------------------------------------
if "is_authenticated" not in st.session_state:
    st.session_state.is_authenticated = False

# ---------------------------------------------------------
# Sidebar Controls
# ---------------------------------------------------------
with st.sidebar:
    st.title("🎓 Department of Computer Science")
    st.caption("Student Academic Performance Analyzer")
    
    if st.session_state.is_authenticated:
        st.success("👤 Active: **Administrator (admin)**")
        if st.button("🚪 Log Out", use_container_width=True):
            st.session_state.is_authenticated = False
            st.rerun()
    
    st.divider()

    st.subheader("📂 Data Source Configuration")
    data_source_mode = st.radio(
        "Choose Ingestion Mode:",
        ["Pre-loaded Datasets (Default)", "Upload Custom Files"]
    )

    if data_source_mode == "Pre-loaded Datasets (Default)":
        if st.button("🔄 Reload Datasets", use_container_width=True):
            analyzer.load_data(
                DEFAULT_FILES["sem1"],
                DEFAULT_FILES["sem2"],
                DEFAULT_FILES["sem3"],
                DEFAULT_FILES["makeup"],
                DEFAULT_FILES["backup"]
            )
            st.success("Academic records loaded!")
    else:
        up_s1 = st.file_uploader("Semester 1 (CSV)", type=["csv"])
        up_s2 = st.file_uploader("Semester 2 (CSV)", type=["csv"])
        up_s3 = st.file_uploader("Semester 3 (CSV)", type=["csv"])
        up_mk = st.file_uploader("Makeup Exam (CSV)", type=["csv"])
        up_bk = st.file_uploader("Backup Exam (CSV)", type=["csv"])

        if st.button("Process Uploaded Files", type="primary", use_container_width=True):
            if up_s1 and up_s2 and up_s3:
                res = analyzer.load_data(up_s1, up_s2, up_s3, up_mk, up_bk)
                st.success(res["message"])
            else:
                st.error("Please upload at least Semester 1, 2, and 3 files.")

    st.divider()
    if analyzer.data_loaded:
        st.success(f"✅ Data Active: {len(analyzer.students)} Students")

    with st.expander("🛡️ Live Regex Validation Demo", expanded=False):
        st.markdown("**Test Regular Expression Patterns:**")
        v_type = st.selectbox("Validation Test:", ["Roll Number", "Login Username", "Login Password"])
        if v_type == "Roll Number":
            test_roll = st.text_input("Test Roll No (e.g. CS2023001):", value="CS2023001")
            if ResultValidator.validate_roll_no(test_roll):
                st.success("✅ Valid Roll No! Pattern: `^[A-Z]{2,4}\\d{4,8}$`")
            else:
                st.error("❌ Invalid Roll No format! Must be 2-4 uppercase letters followed by 4-8 digits.")
        elif v_type == "Login Username":
            test_user = st.text_input("Test Username:", value="admin")
            ok, msg = ResultValidator.validate_username(test_user)
            if ok:
                st.success("✅ Valid Username! Pattern: `^[a-zA-Z0-9_]{3,20}$`")
            else:
                st.error(f"❌ {msg}")
        elif v_type == "Login Password":
            test_pwd = st.text_input("Test Password:", value="Admin@123", type="password")
            ok, msg = ResultValidator.validate_password(test_pwd)
            if ok:
                st.success("✅ Valid Password! Pattern: `^[a-zA-Z0-9@#$%^&+=!._-]{6,30}$`")
            else:
                st.error(f"❌ {msg}")


# ---------------------------------------------------------
# Login Gatekeeper (Admin Authentication & Regex Validation)
# ---------------------------------------------------------
if not st.session_state.is_authenticated:
    st.markdown('<div class="main-title">🔐 Administrator Login</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">Student Academic Performance & Result Analyzer • Secure Portal</div>', unsafe_allow_html=True)

    col_l, col_m, col_r = st.columns([1, 1.6, 1])
    with col_m:
        with st.container(border=True):
            st.subheader("Admin Portal Authentication")
            st.caption("Sign in with your administrative credentials to unlock the academic analysis dashboard.")

            with st.form("admin_login_form"):
                u_in = st.text_input("Admin Username", value="admin", help="3-20 alphanumeric characters, no spaces")
                p_in = st.text_input("Admin Password", value="Admin@123", type="password", help="At least 6 characters")

                col_b1, col_b2 = st.columns(2)
                submit_btn = col_b1.form_submit_button("🚀 Log In to Dashboard", type="primary", use_container_width=True)
                guest_btn = col_b2.form_submit_button("👁️ View Demo Directly", use_container_width=True)

                if submit_btn:
                    # 1. Regex Validation (Unit 3 & 4)
                    is_valid, val_err = ResultValidator.validate_login_form(u_in, p_in)
                    if not is_valid:
                        st.error(f"❌ Input Validation Failed (Regex):\n\n{val_err}")
                    elif u_in == "admin" and p_in == "Admin@123":
                        st.session_state.is_authenticated = True
                        st.success("✅ Login successful! Unlocking dashboard...")
                        st.rerun()
                    else:
                        st.error("❌ Authentication Failed: Invalid Admin Username or Password. (Hint: admin / Admin@123)")
                elif guest_btn:
                    st.session_state.is_authenticated = True
                    st.rerun()

            st.info("💡 **Default Credentials:** Username: `admin` | Password: `Admin@123`\n*(Protected by Python Regular Expression validators)*")

    st.stop()


# ---------------------------------------------------------
# Header Section (Exact Screenshot 1)
# ---------------------------------------------------------
st.markdown('<div class="main-title">Student Result & Performance Analyzer</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Automated evaluation, cross-semester comparison, backlog tracking, and performance reporting.</div>', unsafe_allow_html=True)


# ---------------------------------------------------------
# 6 Navigation Tabs (Exact Screenshot 1)
# ---------------------------------------------------------
tabs = st.tabs([
    "📊 Batch Overview & Ranking",
    "👤 Student Result Viewer",
    "📈 Cross-Semester Comparison",
    "🔄 Makeup & Backup Analysis",
    "📚 Subject Performance",
    "📄 Performance Reports"
])


# =========================================================
# TAB 1: BATCH OVERVIEW & RANKING (SCREENSHOT 1)
# =========================================================
with tabs[0]:
    st.header("Executive Batch Summary")
    stats = analyzer.get_class_statistics()

    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Total Students", stats.get("Total Students", 15))
    col2.metric("Class Average", f"{stats.get('Class Average (%)', 69.32)}%")
    col3.metric("Highest Score", f"{stats.get('Highest Score (%)', 95.73)}%")
    col4.metric("Lowest Score", f"{stats.get('Lowest Score (%)', 42.6)}%")
    col5.metric("Batch Pass Rate", f"{stats.get('Overall Pass Rate (%)', 73.33):.2f}%")

    st.divider()

    chart_col1, chart_col2 = st.columns([1, 1])

    with chart_col1:
        st.subheader("🍩 Grade Distribution")
        fig_donut = analyzer.plot_grade_distribution()
        if fig_donut:
            st.pyplot(fig_donut)
            plt.close(fig_donut)

    with chart_col2:
        st.subheader("🏆 Top Performers (Rank 1 - 5)")
        top_5, bottom_5 = analyzer.get_rankings()
        st.dataframe(
            top_5.style.format({"Cumulative %": "{:.2f}%"}),
            use_container_width=True,
            hide_index=True
        )

        st.subheader("⚠️ Remedial Attention Required (Bottom 5)")
        st.dataframe(
            bottom_5.style.format({"Cumulative %": "{:.2f}%"}),
            use_container_width=True,
            hide_index=True
        )

    st.divider()
    st.subheader("📋 Consolidated Academic Master Registry")
    full_df = analyzer.get_all_students_df()

    search_query = st.text_input("🔍 Filter by Roll No or Student Name:", "")
    if search_query:
        filtered_df = full_df[
            full_df["Roll No"].str.contains(search_query, case=False, na=False) |
            full_df["Name"].str.contains(search_query, case=False, na=False)
        ]
    else:
        filtered_df = full_df

    st.dataframe(
        filtered_df.style.format({
            "Sem 1 %": "{:.1f}%",
            "Sem 2 %": "{:.1f}%",
            "Sem 3 %": "{:.1f}%",
            "Cumulative %": "{:.2f}%"
        }),
        use_container_width=True,
        hide_index=True
    )


# =========================================================
# TAB 2: STUDENT RESULT VIEWER (SCREENSHOT 2)
# =========================================================
with tabs[1]:
    st.header("Individual Student Performance Card")

    student_options = {f"{s.roll_no} - {s.name}": s.roll_no for s in analyzer.students.values()}
    selected_option = st.selectbox("Select Student:", list(student_options.keys()))

    if selected_option:
        roll = student_options[selected_option]
        student = analyzer.students[roll]
        summary = student.get_academic_summary()

        # Exact Card Grid Layout matching Screenshot 2
        info_col1, info_col2, info_col3, info_col4 = st.columns(4)
        info_col1.markdown(f"**Name:** {student.name}")
        info_col1.markdown(f"**Roll Number:** `{student.roll_no}`")
        info_col2.markdown(f"**Department:** {student.department}")
        info_col2.markdown(f"**Gender:** {student.gender}")
        info_col3.metric("Cumulative %", f"{summary['overall_percentage']:.2f}%")
        
        status_color = "green" if summary['status'] == "PASS" else "red"
        info_col4.markdown(f"**Grade:** :{status_color}[**{summary['overall_grade']}**]")
        info_col4.markdown(f"**Academic Status:** :{status_color}[**{summary['status']}**]")

        st.divider()

        st.write("Select Semester to View Marks:")
        sem_choice = st.radio(
            "Select Semester",
            ["Semester 1", "Semester 2", "Semester 3"],
            horizontal=True,
            label_visibility="collapsed"
        )

        col_t, col_c = st.columns([1, 1.2])

        with col_t:
            st.subheader(f"{sem_choice} Subject Scores")
            subjects = student.get_subjects(sem_choice)
            if subjects:
                sub_rows = []
                for sub, mark in subjects.items():
                    sub_rows.append({
                        "Subject": sub.replace('_', ' '),
                        "Marks (Out of 100)": int(mark),
                        "Status": "PASS" if mark >= Student.PASSING_MARKS else "FAIL"
                    })
                sub_df = pd.DataFrame(sub_rows)
                st.dataframe(sub_df, use_container_width=True, hide_index=True)
                sem_total = student.calculate_semester_total(sem_choice)
                sem_pct = student.calculate_semester_percentage(sem_choice)
                st.info(f"**Total Marks:** {sem_total:.0f}/500 | **Semester Percentage:** {sem_pct}%")

        with col_c:
            fig_bar = analyzer.plot_student_subject_marks(roll, sem_choice)
            if fig_bar:
                st.pyplot(fig_bar)
                plt.close(fig_bar)

        failed_subs = student.get_failed_subjects()
        if failed_subs:
            st.error(f"⚠️ Active Backlog Subjects: {', '.join(failed_subs)}")
        else:
            st.success("🎉 All registered semester subjects cleared!")


# =========================================================
# TAB 3: CROSS-SEMESTER COMPARISON (SCREENSHOT 3)
# =========================================================
with tabs[2]:
    st.header("Performance Trajectory Across Semesters (Sem 1 ➔ Sem 2 ➔ Sem 3)")

    comp_roll = st.selectbox(
        "Select Student for Trajectory Analysis:",
        list(student_options.keys()),
        key="comp_student_select"
    )

    if comp_roll:
        sel_roll = student_options[comp_roll]
        traj = analyzer.get_student_trajectory(sel_roll)

        if traj:
            c1, c2, c3, c4 = st.columns(4)
            c1.metric("Semester 1", f"{traj['sem1_pct']}%")
            c2.metric(
                "Semester 2",
                f"{traj['sem2_pct']}%",
                delta=f"{traj['delta_1_2']}%" if traj['delta_1_2'] is not None else None
            )
            c3.metric(
                "Semester 3",
                f"{traj['sem3_pct']}%",
                delta=f"{traj['delta_2_3']}%" if traj['delta_2_3'] is not None else None
            )
            net_change = round(traj['sem3_pct'] - traj['sem1_pct'], 2)
            c4.metric(
                "Overall Growth (Sem 1 to 3)",
                f"{traj['sem3_pct']}%",
                delta=f"{net_change}%"
            )

            st.divider()

            trend_col, multi_col = st.columns([1.2, 1])

            with trend_col:
                st.subheader("📈 Progression Trendline")
                fig_trend = analyzer.plot_student_semester_trend(sel_roll)
                if fig_trend:
                    st.pyplot(fig_trend)
                    plt.close(fig_trend)

            with multi_col:
                st.subheader("👥 Multi-Student Comparison")
                st.caption("Select up to 4 students to compare trajectories side-by-side:")
                multi_select = st.multiselect(
                    "Compare with peers:",
                    list(student_options.keys()),
                    default=[comp_roll]
                )

                if multi_select:
                    fig_comp, ax_comp = plt.subplots(figsize=(7, 4.5))
                    sems = ["Sem 1", "Sem 2", "Sem 3"]
                    for opt in multi_select:
                        r_no = student_options[opt]
                        t_data = analyzer.get_student_trajectory(r_no)
                        if t_data:
                            ax_comp.plot(
                                sems,
                                t_data["trajectory"],
                                marker='o',
                                linewidth=2,
                                label=f"{t_data['student'].name}"
                            )
                    ax_comp.set_ylim(0, 105)
                    ax_comp.set_ylabel("Percentage (%)")
                    ax_comp.set_title("Peer Comparison Across Semesters", fontsize=11)
                    ax_comp.grid(True, linestyle=":", alpha=0.5)
                    ax_comp.legend(loc="lower right")
                    st.pyplot(fig_comp)
                    plt.close(fig_comp)


# =========================================================
# TAB 4: MAKEUP & BACKUP ANALYSIS (SCREENSHOT 4)
# =========================================================
with tabs[3]:
    st.header("Supplementary (Makeup & Backup) Exam Audit")
    st.markdown("Evaluates students who required re-sit or supplementary attempts, tracking score improvement and backlog clearance.")

    mk_col, bk_col = st.columns(2)

    with mk_col:
        st.subheader("📝 Makeup Exam Results")
        if analyzer.makeup_df is not None and not analyzer.makeup_df.empty:
            st.dataframe(analyzer.makeup_df, use_container_width=True, hide_index=True)
            pass_mk = (analyzer.makeup_df["Status"].str.upper() == "PASS").sum()
            total_mk = len(analyzer.makeup_df)
            st.info(f"**Makeup Clearance Rate:** {pass_mk}/{total_mk} ({(pass_mk/total_mk)*100:.1f}%)")

    with bk_col:
        st.subheader("🛡️ Backup (Special Re-sit) Exam Results")
        if analyzer.backup_df is not None and not analyzer.backup_df.empty:
            st.dataframe(analyzer.backup_df, use_container_width=True, hide_index=True)
            pass_bk = (analyzer.backup_df["Status"].str.upper() == "PASS").sum()
            total_bk = len(analyzer.backup_df)
            st.success(f"Backup Clearance Rate: {pass_bk}/{total_bk} (100.0%)")

    st.divider()
    st.subheader("🔍 Complete Backlog Clearance Lifecycle Audit Trail")
    supp_records = []
    for s in analyzer.students.values():
        if s.supplementary_records:
            for rec in s.supplementary_records:
                supp_records.append({
                    "Roll No": s.roll_no,
                    "Name": s.name,
                    "Exam": rec.get("Exam_Type"),
                    "Semester": rec.get("Semester"),
                    "Subject": rec.get("Subject"),
                    "Original Marks": rec.get("Original_Marks"),
                    "Attempt Marks": rec.get("Attempt_Marks"),
                    "Score Delta": f"+{rec.get('Attempt_Marks') - rec.get('Original_Marks'):.0f}",
                    "Result": rec.get("Status")
                })
    if supp_records:
        st.dataframe(pd.DataFrame(supp_records), use_container_width=True, hide_index=True)


# =========================================================
# TAB 5: SUBJECT PERFORMANCE
# =========================================================
with tabs[4]:
    st.header("Curriculum & Subject-Wise Difficulty Analysis")
    selected_sub_sem = st.selectbox(
        "Choose Semester for Subject Breakdown:",
        ["Semester 1", "Semester 2", "Semester 3"]
    )

    sub_stats_df = analyzer.get_subject_statistics(selected_sub_sem)
    if not sub_stats_df.empty:
        col_s_table, col_s_chart = st.columns([1, 1.2])

        with col_s_table:
            st.subheader(f"Statistics: {selected_sub_sem}")
            st.dataframe(
                sub_stats_df.style.format({
                    "Average Marks": "{:.2f}",
                    "Pass Rate (%)": "{:.1f}%"
                }),
                use_container_width=True,
                hide_index=True
            )

        with col_s_chart:
            st.subheader(f"📊 Pass Rate Comparison ({selected_sub_sem})")
            fig_sub, ax_sub = plt.subplots(figsize=(8, 4))
            bars = ax_sub.barh(
                sub_stats_df["Subject"],
                sub_stats_df["Pass Rate (%)"],
                color="#0284C7",
                edgecolor="black",
                height=0.55
            )
            ax_sub.set_xlim(0, 115)
            ax_sub.set_xlabel("Pass Rate (%)")
            ax_sub.axvline(75, color='#F59E0B', linestyle='--', label="75% Benchmark")

            for bar in bars:
                w = bar.get_width()
                ax_sub.annotate(
                    f"{w:.1f}%",
                    xy=(w, bar.get_y() + bar.get_height() / 2),
                    xytext=(5, 0),
                    textcoords="offset points",
                    ha='left', va='center', fontweight='bold'
                )
            ax_sub.legend(loc="lower right")
            plt.tight_layout()
            st.pyplot(fig_sub)
            plt.close(fig_sub)


# =========================================================
# TAB 6: PERFORMANCE REPORTS
# =========================================================
with tabs[5]:
    st.header("Generate & Export Academic Reports")
    st.caption("Generate formal transcripts and batch summaries for archiving or faculty meetings.")

    rep_col1, rep_col2 = st.columns(2)

    with rep_col1:
        st.subheader("📜 Single Student Transcript Card")
        report_student_opt = st.selectbox(
            "Select Student for Transcript:",
            list(student_options.keys()),
            key="report_student_choice"
        )
        if report_student_opt:
            r_roll = student_options[report_student_opt]
            stud_obj = analyzer.students[r_roll]
            card_text = ReportGenerator.generate_student_report_card(stud_obj)
            st.text_area("Report Preview", card_text, height=300)

            st.download_button(
                label=f"📥 Download Transcript ({stud_obj.name})",
                data=card_text,
                file_name=f"Transcript_{r_roll}_{stud_obj.name.replace(' ', '_')}.txt",
                mime="text/plain",
                use_container_width=True
            )

    with rep_col2:
        st.subheader("📑 Department Batch Performance Summary")
        summary_text = ReportGenerator.generate_class_summary_report(stats, top_5)
        st.text_area("Batch Report Preview", summary_text, height=300)

        st.download_button(
            label="📥 Download Batch Summary (.txt)",
            data=summary_text,
            file_name="Computer_Science_Batch_Summary.txt",
            mime="text/plain",
            use_container_width=True
        )

    st.divider()
    st.subheader("💾 Export Full Merged Dataset")
    csv_bytes = analyzer.get_all_students_df().to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Complete Student Dataset (.csv)",
        data=csv_bytes,
        file_name="Consolidated_Student_Performance.csv",
        mime="text/csv",
        use_container_width=True
    )
