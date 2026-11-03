"""
Validation & Regex Utility Module
Provides regex validation patterns and custom exceptions for data integrity.
"""
import re
from typing import Dict, List, Tuple


class DataValidationError(Exception):
    """Raised when academic records fail validation constraints."""
    pass


class MissingColumnError(Exception):
    """Raised when mandatory columns are missing from uploaded datasets."""
    pass


class ResultValidator:
    """
    Validates student roll numbers, names, scores, and login credentials using Regular Expressions.
    """
    # Regex patterns
    ROLL_NO_PATTERN = re.compile(r"^[A-Z]{2,4}\d{4,8}$", re.IGNORECASE)
    NAME_PATTERN = re.compile(r"^[A-Za-z\s.'-]+$")
    USERNAME_PATTERN = re.compile(r"^[a-zA-Z0-9_]{3,20}$")
    PASSWORD_PATTERN = re.compile(r"^[a-zA-Z0-9@#$%^&+=!._-]{6,30}$")

    @classmethod
    def validate_username(cls, username: str) -> Tuple[bool, str]:
        """
        Validates admin username using Regular Expressions (Syllabus Unit 3 & 4).
        Rules: 3-20 characters, alphanumeric and underscores only, no spaces.
        """
        if not username or not username.strip():
            return False, "Username cannot be empty."
        u = username.strip()
        if len(u) < 3 or len(u) > 20:
            return False, "Username must be between 3 and 20 characters in length."
        if not cls.USERNAME_PATTERN.match(u):
            return False, "Username can only contain letters, numbers, and underscores (no spaces or special symbols)."
        return True, ""

    @classmethod
    def validate_password(cls, password: str) -> Tuple[bool, str]:
        """
        Validates admin password using Regular Expressions (Syllabus Unit 3 & 4).
        Rules: Minimum 6 characters, maximum 30 characters, allowed special symbols.
        """
        if not password:
            return False, "Password cannot be empty."
        if len(password) < 6:
            return False, "Password must be at least 6 characters long."
        if len(password) > 30:
            return False, "Password cannot exceed 30 characters."
        if not cls.PASSWORD_PATTERN.match(password):
            return False, "Password contains unsupported special characters."
        return True, ""

    @classmethod
    def validate_login_form(cls, username: str, password: str) -> Tuple[bool, str]:
        """
        Comprehensive validation of login credentials using regex.
        Returns (True, '') if valid, or (False, error_message) if invalid.
        """
        valid_u, err_u = cls.validate_username(username)
        if not valid_u:
            return False, err_u
        valid_p, err_p = cls.validate_password(password)
        if not valid_p:
            return False, err_p
        return True, ""

    @classmethod
    def validate_roll_no(cls, roll_no: str) -> bool:
        """Validates student roll number format (e.g. CS2023001)."""
        if not roll_no or not isinstance(roll_no, str):
            return False
        return bool(cls.ROLL_NO_PATTERN.match(roll_no.strip()))

    @classmethod
    def validate_name(cls, name: str) -> bool:
        """Validates student name format."""
        if not name or not isinstance(name, str):
            return False
        return bool(cls.NAME_PATTERN.match(name.strip()))

    @classmethod
    def validate_score(cls, score: float, min_val: float = 0.0, max_val: float = 100.0) -> bool:
        """Validates that marks lie within legitimate numerical ranges (0 to 100)."""
        try:
            val = float(score)
            return min_val <= val <= max_val
        except (ValueError, TypeError):
            return False

    @classmethod
    def validate_dataset_columns(cls, df_columns: List[str], required_columns: List[str]) -> Tuple[bool, List[str]]:
        """Verifies presence of mandatory columns in a dataset."""
        missing = [col for col in required_columns if col not in df_columns]
        return len(missing) == 0, missing
