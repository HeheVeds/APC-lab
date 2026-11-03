"""
Django Views for Student Result & Performance Analyzer
Provides all 7 interactive analytical tabs styled identically to Streamlit in Dark Theme (#0E1117),
including embedded Matplotlib Donut/Pie charts, Progression Trend lines, Subject Mastery bars,
student marks breakdowns, backlog audits, downloadable reports, and dynamic CSV uploading.
(Syllabus Unit 4, Practical 12: Django Web Framework).
"""
import os
import sys
import io
import base64
from pathlib import Path
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Ensure root directory is accessible for models and utils
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

from analyzer_app.forms import AdminLoginForm
from models.analyzer import ResultAnalyzer
from utils.report_generator import ReportGenerator

# Initialize Analytical Engine
analyzer = ResultAnalyzer()
data_dir = os.path.join(str(BASE_DIR), "data")
analyzer.load_data(
    os.path.join(data_dir, "semester_1.csv"),
    os.path.join(data_dir, "semester_2.csv"),
    os.path.join(data_dir, "semester_3.csv"),
    os.path.join(data_dir, "makeup_exam.csv"),
    os.path.join(data_dir, "backup_exam.csv")
)


def fig_to_base64_dark(fig):
    """
    Converts a Matplotlib figure into a base64 PNG data URI with Dark Theme styling (#262730).
    Matches the visual aesthetic of the Streamlit dashboard.
    """
    if fig is None:
        return ""
    try:
        fig.patch.set_facecolor('#262730')
        for ax in fig.axes:
            ax.set_facecolor('#262730')
            ax.tick_params(colors='#FAFAFA', which='both', labelsize=8.5)
            if hasattr(ax, 'xaxis') and ax.xaxis and ax.xaxis.label:
                ax.xaxis.label.set_color('#FAFAFA')
            if hasattr(ax, 'yaxis') and ax.yaxis and ax.yaxis.label:
                ax.yaxis.label.set_color('#FAFAFA')
            if hasattr(ax, 'title'):
                ax.title.set_color('#FAFAFA')
                ax.title.set_fontweight('bold')
            for spine in ax.spines.values():
                spine.set_color('#4B5563')
            for t in ax.texts:
                t.set_color('#FAFAFA')
                t.set_fontweight('bold')
            if ax.get_legend():
                leg = ax.get_legend()
                leg.get_frame().set_facecolor('#1F2937')
                leg.get_frame().set_edgecolor('#4B5563')
                for text in leg.get_texts():
                    text.set_color('#FAFAFA')
        buf = io.BytesIO()
        fig.savefig(buf, format='png', dpi=105, bbox_inches='tight', facecolor='#262730', edgecolor='none')
        buf.seek(0)
        b64 = base64.b64encode(buf.read()).decode('utf-8')
        plt.close(fig)
        return f"data:image/png;base64,{b64}"
    except Exception:
        plt.close(fig)
        return ""


@csrf_exempt
def login_view(request):
    """
    Renders Admin Login page in Dark Theme matching Streamlit with Django Regex Validators.
    """
    if request.session.get('is_authenticated'):
        return redirect('/dashboard/')

    error_message = ""
    if request.method == 'POST':
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['username']
            pwd = form.cleaned_data['password']
            if user == "admin" and pwd == "Admin@123":
                request.session['is_authenticated'] = True
                request.session['user'] = user
                return redirect('/dashboard/')
            else:
                error_message = "❌ Authentication Failed: Incorrect Username or Password."
    else:
        form = AdminLoginForm()

    form_html = form.as_p()
    err_html = f"<div style='color: #fca5a5; background: #7f1d1d; border: 1px solid #ef4444; padding: 10px 14px; border-radius: 6px; margin-bottom: 15px;'><b>{error_message}</b></div>" if error_message else ""

    response_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Admin Login - Django Web Server</title>
        <style>
            body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; background-color: #0E1117; color: #FAFAFA; margin: 0; padding: 50px 20px; display: flex; justify-content: center; align-items: center; min-height: 80vh; }}
            .card {{ background: #262730; padding: 35px 30px; border-radius: 12px; box-shadow: 0 10px 35px rgba(0,0,0,0.6); width: 400px; border: 1px solid #374151; }}
            h2 {{ color: #3B82F6; margin-top: 0; margin-bottom: 5px; text-align: center; }}
            p.sub {{ color: #9CA3AF; font-size: 0.9em; text-align: center; margin-bottom: 25px; }}
            label {{ font-weight: bold; color: #E5E7EB; font-size: 0.9em; display: block; margin-top: 12px; }}
            input[type="text"], input[type="password"] {{ width: 100%; padding: 10px; margin-top: 6px; box-sizing: border-box; background: #1F2937; border: 1px solid #4B5563; border-radius: 6px; font-size: 1em; color: #FAFAFA; }}
            input:focus {{ outline: none; border-color: #3B82F6; box-shadow: 0 0 0 2px rgba(59,130,246,0.3); }}
            button {{ background: #FF4B4B; color: white; border: none; padding: 12px; width: 100%; font-weight: bold; cursor: pointer; border-radius: 6px; margin-top: 22px; font-size: 1em; transition: background 0.2s; }}
            button:hover {{ background: #E03E3E; }}
            .errorlist {{ color: #F87171; font-size: 0.85em; padding-left: 20px; margin-top: 4px; }}
            .hint {{ background: #1E293B; padding: 12px; border-radius: 6px; font-size: 0.85em; margin-top: 22px; color: #93C5FD; border: 1px solid #3B82F6; line-height: 1.5; }}
            code {{ background: #0F172A; padding: 2px 6px; border-radius: 4px; color: #38BDF8; font-weight: bold; }}
        </style>
    </head>
    <body>
        <div class="card">
            <h2>🔐 Administrator Login</h2>
            <p class="sub">Student Academic Performance & Result Analyzer<br><small style="color: #60A5FA;">Django Web Server • Port 8000 (Dark Theme)</small></p>
            {err_html}
            <form method="POST">
                <input type="hidden" name="csrfmiddlewaretoken" value="{request.META.get('CSRF_COOKIE', '')}">
                {form_html}
                <button type="submit">🚀 Log In to Dashboard</button>
            </form>
            <div class="hint">
                <b>Default Credentials:</b><br>
                Username: <code>admin</code> | Password: <code>Admin@123</code><br>
                <i>(Strictly validated using Python Regular Expressions)</i>
            </div>
        </div>
    </body>
    </html>
    """
    return HttpResponse(response_content)


@csrf_exempt
def dashboard_view(request):
    """
    Renders the complete 7-tab interactive Django Dashboard styled identically to Streamlit
    in Dark Theme (#0E1117) with embedded Matplotlib pie charts, trend lines, and bar charts.
    """
    if not request.session.get('is_authenticated'):
        return redirect('/')

    upload_msg = ""
    upload_status = ""
    active_tab = "tab1"

    # Handle File Upload and Batch Switch Actions
    if request.method == 'POST':
        if 'upload_csv' in request.POST:
            active_tab = "tab7"
            sem1_f = request.FILES.get('sem1_file')
            sem2_f = request.FILES.get('sem2_file')
            sem3_f = request.FILES.get('sem3_file')
            makeup_f = request.FILES.get('makeup_file')
            backup_f = request.FILES.get('backup_file')

            if not sem1_f or not sem2_f or not sem3_f:
                upload_status = "error"
                upload_msg = "❌ Upload Failed: Semester 1, 2, and 3 CSV files are mandatory!"
            else:
                try:
                    s1_buf = io.BytesIO(sem1_f.read())
                    s2_buf = io.BytesIO(sem2_f.read())
                    s3_buf = io.BytesIO(sem3_f.read())
                    mk_buf = io.BytesIO(makeup_f.read()) if makeup_f else None
                    bk_buf = io.BytesIO(backup_f.read()) if backup_f else None

                    res = analyzer.load_data(s1_buf, s2_buf, s3_buf, mk_buf, bk_buf)
                    if res.get("status") == "Success":
                        upload_status = "success"
                        upload_msg = f"✅ Ingested successfully! {res['message']} All dashboard analytics have been recalculated with the uploaded batch."
                    else:
                        upload_status = "error"
                        upload_msg = f"❌ Error loading datasets: {res.get('message')}"
                except Exception as ex:
                    upload_status = "error"
                    upload_msg = f"❌ Parsing Error: {str(ex)}"

        elif 'load_sample_batch' in request.POST:
            active_tab = "tab7"
            test_dir = os.path.join(str(BASE_DIR), "test_upload_samples")
            res = analyzer.load_data(
                os.path.join(test_dir, "test_batch_semester_1.csv"),
                os.path.join(test_dir, "test_batch_semester_2.csv"),
                os.path.join(test_dir, "test_batch_semester_3.csv")
            )
            upload_status = "success"
            upload_msg = "⚡ Successfully loaded Sample IT Test Batch (10 Students)! Check Tabs 1 to 5 to review updated analytics."

        elif 'reset_default' in request.POST:
            active_tab = "tab7"
            analyzer.load_data(
                os.path.join(data_dir, "semester_1.csv"),
                os.path.join(data_dir, "semester_2.csv"),
                os.path.join(data_dir, "semester_3.csv"),
                os.path.join(data_dir, "makeup_exam.csv"),
                os.path.join(data_dir, "backup_exam.csv")
            )
            upload_status = "success"
            upload_msg = "🔄 Successfully reloaded original default academic datasets (15 CS Students)!"

    stats = analyzer.get_class_statistics()
    top_5, bottom_5 = analyzer.get_rankings()
    all_df = analyzer.get_all_students_df()

    # Generate Matplotlib Visualizations in Dark Theme
    pie_chart_b64 = fig_to_base64_dark(analyzer.plot_grade_distribution())
    
    sample_roll = top_5.iloc[0]["Roll No"] if not top_5.empty else "CS2023001"
    trend_chart_b64 = fig_to_base64_dark(analyzer.plot_student_semester_trend(sample_roll))

    # Subject Difficulty Chart for Tab 5
    def _make_subject_overview_chart():
        df_sub = analyzer.get_subject_statistics("Semester 1")
        if df_sub.empty:
            return None
        fig, ax = plt.subplots(figsize=(7.5, 3.2))
        subs = [s.replace('_', ' ') for s in df_sub["Subject"].tolist()]
        avgs = df_sub["Average Marks"].tolist()
        bars = ax.bar(subs, avgs, color="#3B82F6", width=0.55, edgecolor="#60A5FA", linewidth=0.8)
        ax.axhline(75, color="#10B981", linestyle="--", linewidth=1.2, label="Institutional Benchmark (75%)")
        for b in bars:
            h = b.get_height()
            ax.annotate(f"{h:.1f}", (b.get_x() + b.get_width()/2, h + 1), ha='center', fontsize=9, fontweight='bold')
        ax.set_ylim(0, 105)
        ax.set_ylabel("Average Marks", fontsize=9)
        ax.set_title("Semester 1 Subject Performance Averages", fontsize=11, pad=10)
        ax.legend(loc='lower right', fontsize=8)
        plt.xticks(rotation=15, ha='right', fontsize=9)
        plt.tight_layout()
        return fig

    subject_chart_b64 = fig_to_base64_dark(_make_subject_overview_chart())

    upload_banner_html = ""
    if upload_msg:
        if upload_status == "success":
            upload_banner_html = f"<div style='background: #064e3b; color: #6ee7b7; border: 1px solid #10b981; padding: 14px 18px; border-radius: 8px; margin-bottom: 20px; font-weight: bold;'>{upload_msg}</div>"
        else:
            upload_banner_html = f"<div style='background: #7f1d1d; color: #fca5a5; border: 1px solid #ef4444; padding: 14px 18px; border-radius: 8px; margin-bottom: 20px; font-weight: bold;'>{upload_msg}</div>"

    # Tab 1: Ranking Rows
    top_rows = "".join([f"<tr><td><span style='color: #60a5fa; font-weight: bold;'>#{i+1}</span></td><td><code>{r['Roll No']}</code></td><td><b>{r['Name']}</b></td><td><b style='color: #34d399;'>{r['Cumulative %']}%</b></td><td><span style='background: #065f46; color: #6ee7b7; padding: 2px 8px; border-radius: 4px; font-weight: bold;'>{r['Grade']}</span></td></tr>" for i, r in top_5.iterrows()])
    bottom_rows = "".join([f"<tr><td><span style='color: #f87171; font-weight: bold;'>#{i+1}</span></td><td><code>{r['Roll No']}</code></td><td><b>{r['Name']}</b></td><td>{r['Cumulative %']}%</td><td><span style='background: #7f1d1d; color: #fca5a5; padding: 2px 8px; border-radius: 4px; font-weight: bold;'>{r['Status']}</span></td></tr>" for i, r in bottom_5.iterrows()])

    # Tab 1: Master Registry Rows
    master_rows = ""
    for _, r in all_df.iterrows():
        st_color = "#34d399" if r['Status'] == "PASS" else "#fca5a5"
        st_bg = "#064e3b" if r['Status'] == "PASS" else "#7f1d1d"
        master_rows += f"""<tr>
            <td><code>{r['Roll No']}</code></td>
            <td><b>{r['Name']}</b></td>
            <td>{r['Department']}</td>
            <td>{r['Sem 1 %']}%</td>
            <td>{r['Sem 2 %']}%</td>
            <td>{r['Sem 3 %']}%</td>
            <td><b style='color: #60a5fa;'>{r['Cumulative %']}%</b></td>
            <td><span style='background: #1f2937; color: #f3f4f6; padding: 2px 7px; border-radius: 4px; font-weight: bold;'>{r['Grade']}</span></td>
            <td><span style='background: {st_bg}; color: {st_color}; padding: 3px 8px; border-radius: 4px; font-weight: bold; font-size: 0.85em;'>{r['Status']}</span></td>
        </tr>"""

    # Tab 2: Student Cards HTML
    student_cards_html = ""
    student_dropdown_options = ""
    for roll, s in analyzer.students.items():
        summary = s.get_academic_summary()
        student_dropdown_options += f"<option value='{roll}'>{roll} - {s.name}</option>"

        sem1_subs = s.get_subjects("Semester 1")
        sem2_subs = s.get_subjects("Semester 2")
        sem3_subs = s.get_subjects("Semester 3")

        def _sub_table(subs):
            if not subs: return "<i>No records</i>"
            rows = ""
            for sub, m in subs.items():
                clr = "#34d399" if m >= 40 else "#f87171"
                lbl = "PASS" if m >= 40 else "FAIL"
                rows += f"<tr><td>{sub.replace('_', ' ')}</td><td><b>{m}</b></td><td style='color: {clr}; font-weight: bold;'>{lbl}</td></tr>"
            return f"<table style='width: 100%; font-size: 0.88em;'><thead><tr><th>Subject</th><th>Marks</th><th>Status</th></tr></thead><tbody>{rows}</tbody></table>"

        backlog_txt = f"<span style='color: #f87171; font-weight: bold;'>Active Backlogs: {', '.join(summary['backlogs'])}</span>" if summary['backlogs'] else "<span style='color: #34d399; font-weight: bold;'>🎉 All Registered Subjects Cleared!</span>"
        
        # Student marks bar chart for Semester 1
        s_chart_b64 = fig_to_base64_dark(analyzer.plot_student_subject_marks(roll, "Semester 1"))

        student_cards_html += f"""
        <div id="student_card_{roll}" class="student-card-panel" style="display: none;">
            <div style="background: #262730; border-radius: 8px; padding: 22px; border: 1px solid #374151; margin-top: 15px;">
                <div style="display: flex; justify-content: space-between; border-bottom: 2px solid #374151; padding-bottom: 14px; margin-bottom: 16px;">
                    <div>
                        <h3 style="margin: 0; color: #60a5fa;">{s.name} (<code>{roll}</code>)</h3>
                        <p style="margin: 4px 0 0; color: #9ca3af;">Department of {s.department} | Gender: {s.gender}</p>
                    </div>
                    <div style="text-align: right;">
                        <h3 style="margin: 0; color: #34d399;">Cumulative: {summary['overall_percentage']}%</h3>
                        <p style="margin: 4px 0 0; color: #e5e7eb;">Grade: <b>{summary['overall_grade']}</b> | Status: <b>{summary['status']}</b></p>
                    </div>
                </div>
                <div style="margin-bottom: 16px;"><b>Academic Standing:</b> {backlog_txt}</div>
                
                <div style="display: flex; gap: 20px;">
                    <!-- Left: Semester Marks Tables -->
                    <div style="flex: 1.1; display: flex; flex-direction: column; gap: 12px;">
                        <div style="background: #1f2937; padding: 12px; border-radius: 6px; border: 1px solid #374151;">
                            <h4 style="margin: 0 0 8px; color: #60a5fa;">Semester 1 ({s.calculate_semester_percentage('Semester 1')}%)</h4>
                            {_sub_table(sem1_subs)}
                        </div>
                        <div style="background: #1f2937; padding: 12px; border-radius: 6px; border: 1px solid #374151;">
                            <h4 style="margin: 0 0 8px; color: #60a5fa;">Semester 2 ({s.calculate_semester_percentage('Semester 2')}%)</h4>
                            {_sub_table(sem2_subs)}
                        </div>
                        <div style="background: #1f2937; padding: 12px; border-radius: 6px; border: 1px solid #374151;">
                            <h4 style="margin: 0 0 8px; color: #60a5fa;">Semester 3 ({s.calculate_semester_percentage('Semester 3')}%)</h4>
                            {_sub_table(sem3_subs)}
                        </div>
                    </div>

                    <!-- Right: Subject Score Bar Chart -->
                    <div style="flex: 1; background: #1f2937; padding: 15px; border-radius: 6px; border: 1px solid #374151; display: flex; flex-direction: column; justify-content: center; align-items: center;">
                        <h4 style="margin: 0 0 10px 0; color: #60a5fa; align-self: flex-start;">📊 Semester 1 Subject Mastery Chart</h4>
                        <img src="{s_chart_b64}" style="width: 100%; border-radius: 6px; display: block; border: 1px solid #374151;" alt="Marks Chart">
                        <div style="margin-top: 15px; width: 100%; text-align: right;">
                            <a href="/download/transcript/{roll}/" class="btn-action">📥 Download Official Transcript (.txt)</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        """

    # Tab 3: Cross-Semester Progression Rows
    comp_rows = ""
    for roll, s in analyzer.students.items():
        traj = analyzer.get_student_trajectory(roll)
        if traj:
            d12 = f"+{traj['delta_1_2']}%" if traj['delta_1_2'] and traj['delta_1_2'] > 0 else f"{traj['delta_1_2']}%"
            d23 = f"+{traj['delta_2_3']}%" if traj['delta_2_3'] and traj['delta_2_3'] > 0 else f"{traj['delta_2_3']}%"
            net = round(traj['sem3_pct'] - traj['sem1_pct'], 2)
            net_str = f"+{net}%" if net > 0 else f"{net}%"
            trend = "📈 Improved" if net > 0 else ("📉 Declined" if net < 0 else "⭐ Consistent")
            comp_rows += f"""<tr>
                <td><code>{roll}</code></td>
                <td><b>{s.name}</b></td>
                <td>{traj['sem1_pct']}%</td>
                <td>{traj['sem2_pct']}%</td>
                <td>{traj['sem3_pct']}%</td>
                <td style='color: {"#34d399" if traj["delta_1_2"] and traj["delta_1_2"] >= 0 else "#f87171"};'><b>{d12}</b></td>
                <td style='color: {"#34d399" if traj["delta_2_3"] and traj["delta_2_3"] >= 0 else "#f87171"};'><b>{d23}</b></td>
                <td style='color: {"#34d399" if net >= 0 else "#f87171"};'><b>{net_str}</b></td>
                <td>{trend}</td>
            </tr>"""

    # Tab 4: Supplementary Exam Rows
    makeup_rows = ""
    if analyzer.makeup_df is not None and not analyzer.makeup_df.empty:
        for _, r in analyzer.makeup_df.iterrows():
            st_clr = "#34d399" if str(r['Status']).upper() == "PASS" else "#f87171"
            makeup_rows += f"<tr><td><code>{r['Roll_No']}</code></td><td><b>{r['Name']}</b></td><td>{r.get('Semester', 'Sem 1')}</td><td>{r.get('Subject')}</td><td>{r.get('Original_Marks')}</td><td><b style='color: #60a5fa;'>{r.get('Makeup_Marks')}</b></td><td style='color: {st_clr}; font-weight: bold;'>{r.get('Status')}</td></tr>"

    backup_rows = ""
    if analyzer.backup_df is not None and not analyzer.backup_df.empty:
        for _, r in analyzer.backup_df.iterrows():
            st_clr = "#34d399" if str(r['Status']).upper() == "PASS" else "#f87171"
            backup_rows += f"<tr><td><code>{r['Roll_No']}</code></td><td><b>{r['Name']}</b></td><td>{r.get('Semester', 'Sem 2')}</td><td>{r.get('Subject')}</td><td>{r.get('Original_Marks')}</td><td>{r.get('Makeup_Marks')}</td><td><b style='color: #34d399;'>{r.get('Backup_Marks')}</b></td><td style='color: {st_clr}; font-weight: bold;'>{r.get('Status')}</td></tr>"

    # Tab 5: Subject Rows
    def _render_subject_rows(sem_name):
        df_sub = analyzer.get_subject_statistics(sem_name)
        rows = ""
        for _, r in df_sub.iterrows():
            pass_clr = "#34d399" if r['Pass Rate (%)'] >= 75 else "#f87171"
            rows += f"<tr><td><b>{r['Subject']}</b></td><td>{r['Average Marks']}</td><td><span style='color: #60a5fa; font-weight: bold;'>{r['Highest Marks']}</span></td><td>{r['Lowest Marks']}</td><td>{r['Pass Count']}</td><td style='color: {pass_clr}; font-weight: bold;'>{r['Pass Rate (%)']}%</td></tr>"
        return rows

    s1_subject_rows = _render_subject_rows("Semester 1")
    s2_subject_rows = _render_subject_rows("Semester 2")
    s3_subject_rows = _render_subject_rows("Semester 3")

    # Full HTML Response in Dark Theme Matching Streamlit
    response_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Student Result & Performance Analyzer - Django Dashboard</title>
        <style>
            body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; background: #0E1117; color: #FAFAFA; margin: 0; padding: 25px; }}
            
            /* Header */
            .header-bar {{ display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 22px; }}
            .main-title {{ font-size: 2.2rem; font-weight: 700; color: #2563EB; margin: 0 0 4px 0; }}
            .sub-title {{ font-size: 1.02rem; color: #9CA3AF; margin: 0; }}
            .user-badge {{ background: #262730; padding: 10px 18px; border-radius: 8px; border: 1px solid #374151; display: flex; align-items: center; gap: 15px; }}
            
            /* KPI Stats Bar */
            .stats-bar {{ display: flex; gap: 14px; margin-bottom: 24px; }}
            .stat-box {{ background: #262730; border: 1px solid #374151; padding: 16px 14px; border-radius: 8px; flex: 1; text-align: center; }}
            .stat-box p {{ margin: 0 0 6px 0; color: #9CA3AF; font-size: 0.8em; font-weight: bold; letter-spacing: 0.05em; text-transform: uppercase; }}
            .stat-box h3 {{ margin: 0; font-size: 1.85em; color: #FAFAFA; font-weight: 700; }}

            /* Tabs Navigation */
            .tabs-nav {{ display: flex; gap: 6px; border-bottom: 2px solid #374151; margin-bottom: 24px; }}
            .tab-btn {{ background: transparent; border: none; padding: 12px 18px; font-size: 0.95em; font-weight: 600; color: #9CA3AF; cursor: pointer; border-bottom: 3px solid transparent; transition: all 0.2s; }}
            .tab-btn:hover {{ color: #FAFAFA; }}
            .tab-btn.active {{ color: #FAFAFA; border-bottom: 3px solid #FF4B4B; background: #262730; border-radius: 6px 6px 0 0; }}
            .tab-content {{ display: none; }}
            .tab-content.active {{ display: block; }}

            /* Tables */
            table {{ width: 100%; border-collapse: collapse; background: #262730; border-radius: 8px; overflow: hidden; border: 1px solid #374151; margin-top: 10px; margin-bottom: 24px; }}
            th, td {{ padding: 12px 14px; text-align: left; border-bottom: 1px solid #374151; }}
            th {{ background: #1F2937; color: #F3F4F6; font-size: 0.85em; text-transform: uppercase; letter-spacing: 0.04em; }}
            tr:nth-child(even) {{ background: #22252C; }}
            tr:hover {{ background: #2D323E; }}
            code {{ background: #111827; color: #93C5FD; padding: 2px 6px; border-radius: 4px; font-size: 0.92em; }}

            /* Buttons */
            .btn-action {{ background: #2563EB; color: white; text-decoration: none; padding: 8px 14px; border-radius: 6px; font-weight: 600; font-size: 0.88em; display: inline-block; transition: background 0.2s; }}
            .btn-action:hover {{ background: #1D4ED8; }}
            .btn-logout {{ background: #FF4B4B; color: white; text-decoration: none; padding: 7px 14px; border-radius: 6px; font-weight: bold; font-size: 0.85em; transition: background 0.2s; }}
            .btn-logout:hover {{ background: #E03E3E; }}
        </style>
        <script>
            function switchTab(tabId) {{
                document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
                document.querySelectorAll('.tab-content').forEach(content => content.classList.remove('active'));
                const targetBtn = document.getElementById('btn_' + tabId);
                const targetTab = document.getElementById('tab_' + tabId);
                if (targetBtn && targetTab) {{
                    targetBtn.classList.add('active');
                    targetTab.classList.add('active');
                }}
            }}
            function showStudentCard(roll) {{
                document.querySelectorAll('.student-card-panel').forEach(card => card.style.display = 'none');
                if (roll) {{
                    const el = document.getElementById('student_card_' + roll);
                    if (el) {{ el.style.display = 'block'; }}
                }}
            }}
            window.onload = function() {{
                const sel = document.getElementById('studentSelect');
                if (sel && sel.value) {{ showStudentCard(sel.value); }}
            }};
        </script>
    </head>
    <body>
        <!-- Header Section -->
        <div class="header-bar">
            <div>
                <h1 class="main-title">🎓 Student Result & Performance Analyzer</h1>
                <p class="sub-title">Automated evaluation, cross-semester comparison, backlog tracking, and performance reporting • Port 8000</p>
            </div>
            <div class="user-badge">
                <span style="color: #93C5FD; font-size: 0.9em;">👤 Admin: <b>admin</b></span>
                <a href="/logout/" class="btn-logout">🚪 Logout</a>
            </div>
        </div>

        <!-- 5 Key KPI Metric Cards -->
        <div class="stats-bar">
            <div class="stat-box">
                <p>Total Students</p>
                <h3>{stats.get('Total Students', 0)}</h3>
            </div>
            <div class="stat-box">
                <p>Class Average</p>
                <h3>{stats.get('Class Average (%)', 0)}%</h3>
            </div>
            <div class="stat-box">
                <p>Highest Score</p>
                <h3 style="color: #60a5fa;">{stats.get('Highest Score (%)', 0)}%</h3>
            </div>
            <div class="stat-box">
                <p>Lowest Score</p>
                <h3 style="color: #f87171;">{stats.get('Lowest Score (%)', 0)}%</h3>
            </div>
            <div class="stat-box">
                <p>Batch Pass Rate</p>
                <h3 style="color: #34d399;">{stats.get('Overall Pass Rate (%)', 0)}%</h3>
            </div>
        </div>

        <!-- 7 Interactive Tabs Navigation -->
        <div class="tabs-nav">
            <button id="btn_tab1" class="tab-btn { 'active' if active_tab == 'tab1' else '' }" onclick="switchTab('tab1')">📊 Batch Overview & Ranking</button>
            <button id="btn_tab2" class="tab-btn { 'active' if active_tab == 'tab2' else '' }" onclick="switchTab('tab2')">👤 Student Result Viewer</button>
            <button id="btn_tab3" class="tab-btn { 'active' if active_tab == 'tab3' else '' }" onclick="switchTab('tab3')">📈 Cross-Semester Comparison</button>
            <button id="btn_tab4" class="tab-btn { 'active' if active_tab == 'tab4' else '' }" onclick="switchTab('tab4')">🔄 Makeup & Backup Analysis</button>
            <button id="btn_tab5" class="tab-btn { 'active' if active_tab == 'tab5' else '' }" onclick="switchTab('tab5')">📚 Subject Performance</button>
            <button id="btn_tab6" class="tab-btn { 'active' if active_tab == 'tab6' else '' }" onclick="switchTab('tab6')">📄 Reports & Downloads</button>
            <button id="btn_tab7" class="tab-btn { 'active' if active_tab == 'tab7' else '' }" onclick="switchTab('tab7')">📂 Upload CSV Datasets</button>
        </div>

        {upload_banner_html}

        <!-- ========================================== -->
        <!-- TAB 1: BATCH OVERVIEW & RANKING -->
        <!-- ========================================== -->
        <div id="tab_tab1" class="tab-content { 'active' if active_tab == 'tab1' else '' }">
            <div style="display: flex; gap: 24px; align-items: flex-start; margin-bottom: 24px;">
                <!-- Left: Embedded Grade Distribution Donut/Pie Chart -->
                <div style="flex: 1; background: #262730; padding: 20px; border-radius: 8px; border: 1px solid #374151; text-align: center;">
                    <h3 style="color: #60a5fa; margin-top: 0; margin-bottom: 15px; text-align: left;">🍩 Grade Distribution (Cohort)</h3>
                    <img src="{pie_chart_b64}" style="width: 100%; max-width: 420px; border-radius: 8px; display: block; margin: 0 auto;" alt="Grade Pie Chart">
                </div>

                <!-- Right: Top 5 & Bottom 5 Rankings -->
                <div style="flex: 1.2; display: flex; flex-direction: column; gap: 18px;">
                    <div>
                        <h3 style="color: #60a5fa; margin-top: 0; margin-bottom: 8px;">🏆 Top Performers (Rank 1 - 5)</h3>
                        <table>
                            <thead><tr><th>Rank</th><th>Roll No</th><th>Name</th><th>Cumulative %</th><th>Grade</th></tr></thead>
                            <tbody>{top_rows}</tbody>
                        </table>
                    </div>
                    <div>
                        <h3 style="color: #f87171; margin-top: 0; margin-bottom: 8px;">⚠️ Remedial Attention Required (Bottom 5)</h3>
                        <table>
                            <thead><tr><th>Rank</th><th>Roll No</th><th>Name</th><th>Cumulative %</th><th>Status</th></tr></thead>
                            <tbody>{bottom_rows}</tbody>
                        </table>
                    </div>
                </div>
            </div>

            <h3 style="color: #60a5fa; margin-top: 25px; margin-bottom: 8px;">📋 Consolidated Academic Master Registry</h3>
            <table>
                <thead><tr><th>Roll No</th><th>Name</th><th>Department</th><th>Sem 1 %</th><th>Sem 2 %</th><th>Sem 3 %</th><th>Cumulative %</th><th>Grade</th><th>Status</th></tr></thead>
                <tbody>{master_rows}</tbody>
            </table>
        </div>

        <!-- ========================================== -->
        <!-- TAB 2: STUDENT RESULT VIEWER -->
        <!-- ========================================== -->
        <div id="tab_tab2" class="tab-content">
            <h3 style="color: #60a5fa; margin-top: 0;">👤 Individual Student Marksheet & Subject Breakdown</h3>
            <div style="background: #262730; padding: 18px; border-radius: 8px; border: 1px solid #374151; display: flex; align-items: center; gap: 15px;">
                <label for="studentSelect" style="font-weight: bold; color: #e5e7eb;">Select Student:</label>
                <select id="studentSelect" onchange="showStudentCard(this.value)" style="padding: 9px 14px; font-size: 1em; border-radius: 6px; border: 1px solid #4b5563; background: #1f2937; color: #fafafa; min-width: 300px;">
                    {student_dropdown_options}
                </select>
                <small style="color: #9ca3af;">Select any student to view their marksheet and mastery bar chart.</small>
            </div>
            {student_cards_html}
        </div>

        <!-- ========================================== -->
        <!-- TAB 3: CROSS-SEMESTER COMPARISON -->
        <!-- ========================================== -->
        <div id="tab_tab3" class="tab-content">
            <h3 style="color: #60a5fa; margin-top: 0;">📈 Performance Progression Across Semesters (Sem 1 ➔ Sem 2 ➔ Sem 3)</h3>
            <p style="color: #9ca3af; font-size: 0.9em; margin-bottom: 20px;">Calculates semester-over-semester growth delta (Δ%) to evaluate whether academic trajectory is improving or declining.</p>
            
            <!-- Embedded Semester Progression Trend Line Chart -->
            <div style="background: #262730; padding: 22px; border-radius: 8px; border: 1px solid #374151; margin-bottom: 25px; text-align: center;">
                <h4 style="margin: 0 0 14px 0; color: #60a5fa; text-align: left;">📈 Cohort Progression Trendline (Sample Student Trajectory)</h4>
                <img src="{trend_chart_b64}" style="width: 100%; max-width: 720px; border-radius: 8px; display: block; margin: 0 auto; border: 1px solid #374151;" alt="Progression Line Chart">
            </div>

            <table>
                <thead><tr><th>Roll No</th><th>Name</th><th>Sem 1 %</th><th>Sem 2 %</th><th>Sem 3 %</th><th>Δ Sem 1-2</th><th>Δ Sem 2-3</th><th>Net Growth</th><th>Trajectory Trend</th></tr></thead>
                <tbody>{comp_rows}</tbody>
            </table>
        </div>

        <!-- ========================================== -->
        <!-- TAB 4: MAKEUP & BACKUP EXAM ANALYSIS -->
        <!-- ========================================== -->
        <div id="tab_tab4" class="tab-content">
            <h3 style="color: #60a5fa; margin-top: 0;">🔄 Supplementary (Makeup & Backup) Exam Audit Trail</h3>
            <p style="color: #9ca3af; font-size: 0.9em; margin-bottom: 18px;">Evaluates students who required re-sit attempts, tracking score improvement from Original Marks ➔ Makeup Exam ➔ Backup Exam.</p>
            
            <h4 style="color: #60a5fa; margin-bottom: 6px;">📝 Makeup Exam Results (1st Supplementary Sitting)</h4>
            <table>
                <thead><tr><th>Roll No</th><th>Name</th><th>Semester</th><th>Subject</th><th>Original Marks</th><th>Makeup Marks</th><th>Status</th></tr></thead>
                <tbody>{makeup_rows}</tbody>
            </table>

            <h4 style="color: #60a5fa; margin-top: 25px; margin-bottom: 6px;">🛡️ Backup Exam Results (2nd Special Re-sit Sitting)</h4>
            <table>
                <thead><tr><th>Roll No</th><th>Name</th><th>Semester</th><th>Subject</th><th>Original Marks</th><th>Makeup Marks</th><th>Backup Marks</th><th>Final Status</th></tr></thead>
                <tbody>{backup_rows}</tbody>
            </table>
        </div>

        <!-- ========================================== -->
        <!-- TAB 5: SUBJECT PERFORMANCE -->
        <!-- ========================================== -->
        <div id="tab_tab5" class="tab-content">
            <h3 style="color: #60a5fa; margin-top: 0;">📚 Subject Difficulty & Curriculum Performance</h3>
            <p style="color: #9ca3af; font-size: 0.9em; margin-bottom: 20px;">Evaluates subject pass rates against an institutional benchmark (75%) to identify curriculum bottlenecks.</p>
            
            <!-- Embedded Subject Performance Bar Chart -->
            <div style="background: #262730; padding: 22px; border-radius: 8px; border: 1px solid #374151; margin-bottom: 25px; text-align: center;">
                <h4 style="margin: 0 0 14px 0; color: #60a5fa; text-align: left;">📊 Subject Performance Averages vs Benchmark</h4>
                <img src="{subject_chart_b64}" style="width: 100%; max-width: 720px; border-radius: 8px; display: block; margin: 0 auto; border: 1px solid #374151;" alt="Subject Bar Chart">
            </div>

            <h4 style="color: #60a5fa; margin-bottom: 6px;">Semester 1 Curriculum Analysis</h4>
            <table>
                <thead><tr><th>Subject Name</th><th>Class Average</th><th>Highest Marks</th><th>Lowest Marks</th><th>Pass Count</th><th>Pass Rate (%)</th></tr></thead>
                <tbody>{s1_subject_rows}</tbody>
            </table>

            <h4 style="color: #60a5fa; margin-top: 25px; margin-bottom: 6px;">Semester 2 Curriculum Analysis</h4>
            <table>
                <thead><tr><th>Subject Name</th><th>Class Average</th><th>Highest Marks</th><th>Lowest Marks</th><th>Pass Count</th><th>Pass Rate (%)</th></tr></thead>
                <tbody>{s2_subject_rows}</tbody>
            </table>

            <h4 style="color: #60a5fa; margin-top: 25px; margin-bottom: 6px;">Semester 3 Curriculum Analysis</h4>
            <table>
                <thead><tr><th>Subject Name</th><th>Class Average</th><th>Highest Marks</th><th>Lowest Marks</th><th>Pass Count</th><th>Pass Rate (%)</th></tr></thead>
                <tbody>{s3_subject_rows}</tbody>
            </table>
        </div>

        <!-- ========================================== -->
        <!-- TAB 6: REPORTS & EXPORT -->
        <!-- ========================================== -->
        <div id="tab_tab6" class="tab-content">
            <h3 style="color: #60a5fa; margin-top: 0;">📄 Generate & Download Academic Reports</h3>
            <div style="display: flex; gap: 20px;">
                <div style="flex: 1; background: #262730; padding: 22px; border-radius: 8px; border: 1px solid #374151;">
                    <h4 style="margin: 0 0 10px; color: #60a5fa;">📑 Department Batch Summary Report</h4>
                    <p style="color: #9ca3af; font-size: 0.9em; line-height: 1.5; margin-bottom: 20px;">Exports a formal executive summary containing total students, batch averages, pass percentages, and topper details for faculty meetings.</p>
                    <a href="/download/class-summary/" class="btn-action">📥 Download Batch Summary (.txt)</a>
                </div>
                <div style="flex: 1; background: #262730; padding: 22px; border-radius: 8px; border: 1px solid #374151;">
                    <h4 style="margin: 0 0 10px; color: #60a5fa;">💾 Consolidated Academic Dataset (.csv)</h4>
                    <p style="color: #9ca3af; font-size: 0.9em; line-height: 1.5; margin-bottom: 20px;">Exports the complete merged academic dataset of all students across all three semesters for external spreadsheet analysis.</p>
                    <a href="/download/csv/" class="btn-action">📥 Download Full Dataset (.csv)</a>
                </div>
            </div>
        </div>

        <!-- ========================================== -->
        <!-- TAB 7: UPLOAD CSV DATASETS -->
        <!-- ========================================== -->
        <div id="tab_tab7" class="tab-content { 'active' if active_tab == 'tab7' else '' }">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 18px;">
                <div>
                    <h3 style="color: #60a5fa; margin: 0;">📂 Upload & Ingest Academic CSV Datasets</h3>
                    <p style="color: #9ca3af; font-size: 0.9em; margin: 5px 0 0;">Upload new semester CSV datasets to dynamically recalculate statistics, rankings, pie charts, and student profiles across all tabs.</p>
                </div>
                <div>
                    <span style="background: #1f2937; color: #60a5fa; padding: 8px 14px; border-radius: 6px; font-weight: bold; font-size: 0.9em; border: 1px solid #374151;">
                        Active Records: {len(analyzer.students)} Students
                    </span>
                </div>
            </div>

            <div style="display: flex; gap: 25px;">
                <!-- Left: Custom Upload Form -->
                <div style="flex: 1.4; background: #262730; padding: 24px; border-radius: 8px; border: 1px solid #374151;">
                    <h4 style="margin-top: 0; color: #60a5fa; border-bottom: 2px solid #374151; padding-bottom: 10px;">📤 Custom Dataset Upload Form</h4>
                    
                    <form method="POST" action="/dashboard/" enctype="multipart/form-data">
                        <input type="hidden" name="upload_csv" value="1">
                        
                        <div style="margin-bottom: 15px;">
                            <label style="display: block; font-weight: bold; color: #e5e7eb; margin-bottom: 5px;">Semester 1 CSV File <span style="color: #f87171;">*</span></label>
                            <input type="file" name="sem1_file" accept=".csv" required style="width: 100%; padding: 8px; border: 1px solid #4b5563; border-radius: 6px; background: #1f2937; color: #fafafa; box-sizing: border-box;">
                            <small style="color: #9ca3af;">Mandatory columns: Roll_No, Name, and subject mark columns.</small>
                        </div>

                        <div style="margin-bottom: 15px;">
                            <label style="display: block; font-weight: bold; color: #e5e7eb; margin-bottom: 5px;">Semester 2 CSV File <span style="color: #f87171;">*</span></label>
                            <input type="file" name="sem2_file" accept=".csv" required style="width: 100%; padding: 8px; border: 1px solid #4b5563; border-radius: 6px; background: #1f2937; color: #fafafa; box-sizing: border-box;">
                        </div>

                        <div style="margin-bottom: 15px;">
                            <label style="display: block; font-weight: bold; color: #e5e7eb; margin-bottom: 5px;">Semester 3 CSV File <span style="color: #f87171;">*</span></label>
                            <input type="file" name="sem3_file" accept=".csv" required style="width: 100%; padding: 8px; border: 1px solid #4b5563; border-radius: 6px; background: #1f2937; color: #fafafa; box-sizing: border-box;">
                        </div>

                        <div style="margin-bottom: 15px;">
                            <label style="display: block; font-weight: bold; color: #e5e7eb; margin-bottom: 5px;">Makeup Exam CSV File <small style="color: #9ca3af;">(Optional)</small></label>
                            <input type="file" name="makeup_file" accept=".csv" style="width: 100%; padding: 8px; border: 1px solid #4b5563; border-radius: 6px; background: #1f2937; color: #fafafa; box-sizing: border-box;">
                        </div>

                        <div style="margin-bottom: 20px;">
                            <label style="display: block; font-weight: bold; color: #e5e7eb; margin-bottom: 5px;">Backup Exam CSV File <small style="color: #9ca3af;">(Optional)</small></label>
                            <input type="file" name="backup_file" accept=".csv" style="width: 100%; padding: 8px; border: 1px solid #4b5563; border-radius: 6px; background: #1f2937; color: #fafafa; box-sizing: border-box;">
                        </div>

                        <button type="submit" style="background: #ff4b4b; color: white; border: none; padding: 12px 20px; font-weight: bold; border-radius: 6px; cursor: pointer; font-size: 1em; width: 100%; transition: background 0.2s;">
                            🚀 Ingest & Process Uploaded Datasets
                        </button>
                    </form>
                </div>

                <!-- Right: Quick Presets & Guidelines -->
                <div style="flex: 1; display: flex; flex-direction: column; gap: 18px;">
                    <!-- Quick Presets -->
                    <div style="background: #262730; padding: 22px; border-radius: 8px; border: 1px solid #374151;">
                        <h4 style="margin-top: 0; color: #60a5fa; margin-bottom: 8px;">⚡ Quick Test Batch Switcher</h4>
                        <p style="color: #9ca3af; font-size: 0.88em; line-height: 1.4; margin-bottom: 16px;">Switch between batches with one click to test dynamic recalculation:</p>
                        
                        <form method="POST" action="/dashboard/" style="margin-bottom: 10px;">
                            <input type="hidden" name="load_sample_batch" value="1">
                            <button type="submit" style="background: #0284c7; color: white; border: none; padding: 10px 15px; font-weight: bold; border-radius: 6px; cursor: pointer; font-size: 0.9em; width: 100%;">
                                ⚡ Load Sample IT Batch (10 Students)
                            </button>
                        </form>

                        <form method="POST" action="/dashboard/">
                            <input type="hidden" name="reset_default" value="1">
                            <button type="submit" style="background: #374151; color: white; border: none; padding: 10px 15px; font-weight: bold; border-radius: 6px; cursor: pointer; font-size: 0.9em; width: 100%;">
                                🔄 Reset to Default CS Batch (15 Students)
                            </button>
                        </form>
                    </div>

                    <!-- Guidelines -->
                    <div style="background: #1f2937; padding: 22px; border-radius: 8px; border: 1px solid #374151;">
                        <h4 style="margin-top: 0; color: #60a5fa; margin-bottom: 8px;">📋 CSV Formatting Rules</h4>
                        <ul style="margin: 0; padding-left: 18px; color: #e5e7eb; font-size: 0.88em; line-height: 1.6;">
                            <li>File format: standard Comma Separated Values (<code>.csv</code>).</li>
                            <li>Required base columns: <code>Roll_No</code>, <code>Name</code>.</li>
                            <li>Subject columns must contain integer or float marks (between 0 and 100).</li>
                            <li>Pre-configured test batches are located in:<br><code>test_upload_samples/</code></li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    return HttpResponse(response_content)


def download_transcript(request, roll_no):
    """Generates and serves downloadable single-student transcript."""
    if not request.session.get('is_authenticated'):
        return redirect('/')
    student = analyzer.students.get(roll_no)
    if not student:
        return HttpResponse("Student not found", status=404)
    content = ReportGenerator.generate_student_report_card(student)
    response = HttpResponse(content, content_type='text/plain; charset=utf-8')
    response['Content-Disposition'] = f'attachment; filename="Transcript_{roll_no}_{student.name.replace(" ", "_")}.txt"'
    return response


def download_class_summary(request):
    """Generates and serves downloadable batch performance report."""
    if not request.session.get('is_authenticated'):
        return redirect('/')
    stats = analyzer.get_class_statistics()
    top_5, _ = analyzer.get_rankings()
    content = ReportGenerator.generate_class_summary_report(stats, top_5)
    response = HttpResponse(content, content_type='text/plain; charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename="Computer_Science_Batch_Summary.txt"'
    return response


def download_csv(request):
    """Serves consolidated master CSV file."""
    if not request.session.get('is_authenticated'):
        return redirect('/')
    csv_bytes = analyzer.get_all_students_df().to_csv(index=False)
    response = HttpResponse(csv_bytes, content_type='text/csv; charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename="Consolidated_Student_Performance.csv"'
    return response


def logout_view(request):
    """Logs user out of Django session."""
    request.session.flush()
    return redirect('/')
