@echo off
title Student Result Analyzer (Django Local Server)
echo ========================================================
echo   Starting Django Local Web Server (Practical 12)
echo ========================================================
cd /d "%~dp0"
echo Server starting at http://127.0.0.1:8000/
start http://127.0.0.1:8000/
python manage.py runserver 127.0.0.1:8000
pause
