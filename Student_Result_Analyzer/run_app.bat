@echo off
title Student Result & Performance Analyzer (Web Dashboard)
echo ========================================================
echo   Starting Student Result & Performance Analyzer
echo   Opening Streamlit Web Dashboard at http://localhost:8501
echo ========================================================
cd /d %~dp0
python -m streamlit run app.py
pause
