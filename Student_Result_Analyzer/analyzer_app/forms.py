"""
Django Forms Module with Regular Expression (Regex) Validation
Directly fulfills Practical 12 of Python Syllabus:
"Creating applications using Django web framework to demonstrate
functionality of user login and its validation using regular expression."
"""
from django import forms
from django.core.validators import RegexValidator


class AdminLoginForm(forms.Form):
    """
    Admin Login Form with strict Regex Validators for username and password.
    """
    username = forms.CharField(
        max_length=20,
        min_length=3,
        required=True,
        label="Admin Username",
        initial="admin",
        validators=[
            RegexValidator(
                regex=r"^[a-zA-Z0-9_]{3,20}$",
                message="Validation Error: Username must be 3-20 characters long and contain only letters, numbers, and underscores (no spaces)."
            )
        ]
    )

    password = forms.CharField(
        max_length=30,
        min_length=6,
        required=True,
        label="Password",
        initial="Admin@123",
        widget=forms.PasswordInput(render_value=True),
        validators=[
            RegexValidator(
                regex=r"^[a-zA-Z0-9@#$%^&+=!._-]{6,30}$",
                message="Validation Error: Password must be at least 6 characters and contain no illegal spaces or characters."
            )
        ]
    )
