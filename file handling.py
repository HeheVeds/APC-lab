
import os
import string
import re


# ============================================================
#                 FILE HANDLING PROGRAMS
# ============================================================

# 1. Create student.txt and write student information
def file_program_1():
    with open("student.txt", "w") as f:
        f.write("Name: Vedika Patil\n")
        f.write("Roll No: 101\n")
        f.write("Branch: Computer Science\n")
        f.write("Semester: 5\n")

    print("student.txt created successfully.")


# 2. Display complete contents of file
def file_program_2():
    try:
        with open("student.txt", "r") as f:
            print("\nFile Contents:")
            print(f.read())
    except FileNotFoundError:
        print("File not found. Run Program 1 first.")


# 3. Append additional information
def file_program_3():
    with open("student.txt", "a") as f:
        f.write("College: D Y Patil College of Engineering and Technology\n")
        f.write("City: Kolhapur\n")

    print("Information appended successfully.")


# 4. Read file line by line
def file_program_4():
    try:
        with open("student.txt", "r") as f:
            print("\nLines in file:")
            for line in f:
                print(line.strip())
    except FileNotFoundError:
        print("File not found.")


# 5. Count total lines
def file_program_5():
    try:
        with open("student.txt", "r") as f:
            lines = f.readlines()

        print("Total lines:", len(lines))
    except FileNotFoundError:
        print("File not found.")


# 6. Count total words
def file_program_6():
    try:
        with open("student.txt", "r") as f:
            text = f.read()

        words = text.split()
        print("Total words:", len(words))
    except FileNotFoundError:
        print("File not found.")


# 7. Count total characters including spaces
def file_program_7():
    try:
        with open("student.txt", "r") as f:
            text = f.read()

        print("Total characters including spaces:", len(text))
    except FileNotFoundError:
        print("File not found.")


# 8. Display lines in reverse order
def file_program_8():
    try:
        with open("student.txt", "r") as f:
            lines = f.readlines()

        print("\nLines in reverse order:")
        for line in reversed(lines):
            print(line.strip())
    except FileNotFoundError:
        print("File not found.")


# 9. Count vowels and consonants
def file_program_9():
    try:
        with open("student.txt", "r") as f:
            text = f.read().lower()

        vowels = 0
        consonants = 0

        for ch in text:
            if ch.isalpha():
                if ch in "aeiou":
                    vowels += 1
                else:
                    consonants += 1

        print("Vowels:", vowels)
        print("Consonants:", consonants)
    except FileNotFoundError:
        print("File not found.")


# 10. Count alphabets, digits, spaces and special characters
def file_program_10():
    try:
        with open("student.txt", "r") as f:
            text = f.read()

        alphabets = 0
        digits = 0
        spaces = 0
        special = 0

        for ch in text:
            if ch.isalpha():
                alphabets += 1
            elif ch.isdigit():
                digits += 1
            elif ch.isspace():
                spaces += 1
            else:
                special += 1

        print("Alphabets:", alphabets)
        print("Digits:", digits)
        print("Spaces:", spaces)
        print("Special characters:", special)

    except FileNotFoundError:
        print("File not found.")


# 11. Find longest word
def file_program_11():
    try:
        with open("student.txt", "r") as f:
            text = f.read()

        words = text.split()

        # Remove punctuation
        clean_words = []
        for word in words:
            word = word.strip(string.punctuation)
            clean_words.append(word)

        longest = max(clean_words, key=len)

        print("Longest word:", longest)
        print("Length:", len(longest))

    except FileNotFoundError:
        print("File not found.")


# 12. Count each word using dictionary
def file_program_12():
    try:
        with open("student.txt", "r") as f:
            text = f.read().lower()

        words = text.split()
        word_count = {}

        for word in words:
            word = word.strip(string.punctuation)

            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

        print("\nWord Frequency:")
        for word, count in word_count.items():
            print(word, ":", count)

    except FileNotFoundError:
        print("File not found.")


# 13. Search word and display occurrences and line numbers
def file_program_13():
    try:
        word = input("Enter word to search: ").lower()

        with open("student.txt", "r") as f:
            lines = f.readlines()

        total = 0

        for i, line in enumerate(lines, start=1):
            words = line.lower().split()
            count = words.count(word)

            if count > 0:
                print("Found in line:", i)
                print("Occurrences in this line:", count)
                total += count

        print("Total occurrences:", total)

        if total == 0:
            print("Word not found.")

    except FileNotFoundError:
        print("File not found.")


# 14. Replace all occurrences of a word
def file_program_14():
    try:
        old_word = input("Enter word to replace: ")
        new_word = input("Enter new word: ")

        with open("student.txt", "r") as f:
            text = f.read()

        text = text.replace(old_word, new_word)

        with open("modified_student.txt", "w") as f:
            f.write(text)

        print("Modified file created: modified_student.txt")

    except FileNotFoundError:
        print("File not found.")


# 15. Remove single-line comments from Python file
def file_program_15():
    source = input("Enter Python source file name: ")

    try:
        with open(source, "r") as f:
            lines = f.readlines()

        with open("without_comments.py", "w") as f:
            for line in lines:
                stripped = line.lstrip()

                if not stripped.startswith("#"):
                    f.write(line)

        print("Comments removed.")
        print("New file: without_comments.py")

    except FileNotFoundError:
        print("Source file not found.")


# 16. Create uppercase copy of text file
def file_program_16():
    try:
        with open("student.txt", "r") as f:
            text = f.read()

        with open("uppercase_student.txt", "w") as f:
            f.write(text.upper())

        print("Uppercase copy created: uppercase_student.txt")

    except FileNotFoundError:
        print("File not found.")


# ============================================================
#                       MODULE PROGRAMS
# ============================================================

# 17. Calculator Module
def module_1_calculator():
    print("\n--- Calculator Module ---")

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)

    if b != 0:
        print("Division:", a / b)
    else:
        print("Division not possible.")


# 18. Student Result Module
def module_2_student():
    print("\n--- Student Result Module ---")

    m1 = float(input("Enter marks of Subject 1: "))
    m2 = float(input("Enter marks of Subject 2: "))
    m3 = float(input("Enter marks of Subject 3: "))

    total = m1 + m2 + m3
    percentage = total / 3

    if percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    else:
        grade = "D"

    print("Total:", total)
    print("Percentage:", percentage)
    print("Grade:", grade)


# 19. Number Utilities Module
def module_3_numbers():
    print("\n--- Number Utilities Module ---")

    n = int(input("Enter number: "))

    # Prime
    prime = True

    if n < 2:
        prime = False

    for i in range(2, n):
        if n % i == 0:
            prime = False
            break

    if prime:
        print("Prime number")
    else:
        print("Not a prime number")

    # Palindrome
    if str(n) == str(n)[::-1]:
        print("Palindrome")
    else:
        print("Not a palindrome")

    # Armstrong
    digits = len(str(n))
    total = 0
    temp = n

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    if total == n:
        print("Armstrong number")
    else:
        print("Not an Armstrong number")

    # Perfect
    total = 0

    for i in range(1, n):
        if n % i == 0:
            total += i

    if total == n:
        print("Perfect number")
    else:
        print("Not a perfect number")


# 20. String Utilities Module
def module_4_strings():
    print("\n--- String Utilities Module ---")

    text = input("Enter a string: ")

    vowels = 0

    for ch in text.lower():
        if ch in "aeiou":
            vowels += 1

    print("Number of vowels:", vowels)
    print("Reverse:", text[::-1])

    if text.lower() == text[::-1].lower():
        print("Palindrome")
    else:
        print("Not a palindrome")

    print("Number of words:", len(text.split()))
    print("Without spaces:", text.replace(" ", ""))


# 21. Recursive Functions Module
def module_5_recursive():
    print("\n--- Recursive Functions Module ---")

    n = int(input("Enter number: "))

    def factorial(n):
        if n == 0 or n == 1:
            return 1
        return n * factorial(n - 1)

    def fibonacci(n):
        if n <= 1:
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)

    def sum_digits(n):
        if n == 0:
            return 0
        return n % 10 + sum_digits(n // 10)

    def binary(n):
        if n == 0:
            return ""
        return binary(n // 2) + str(n % 2)

    print("Factorial:", factorial(n))
    print("Fibonacci:", fibonacci(n))
    print("Sum of digits:", sum_digits(n))

    if n == 0:
        print("Binary: 0")
    else:
        print("Binary:", binary(n))


# ============================================================
#                       PACKAGE PROGRAMS
# ============================================================

# 22. Mathutils Package
def package_1_mathutils():
    print("\n--- Mathutils Package ---")

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)

    numbers = [a, b]

    print("Mean:", sum(numbers) / len(numbers))
    print("Maximum:", max(numbers))
    print("Minimum:", min(numbers))

    n = int(input("Enter number for checking: "))

    # Prime
    prime = True

    if n < 2:
        prime = False

    for i in range(2, n):
        if n % i == 0:
            prime = False
            break

    print("Prime:", prime)

    # Palindrome
    print("Palindrome:", str(n) == str(n)[::-1])

    # Armstrong
    power = len(str(n))
    total = 0
    temp = n

    while temp > 0:
        digit = temp % 10
        total += digit ** power
        temp //= 10

    print("Armstrong:", total == n)


# 23. Student Package
def package_2_student():
    print("\n--- Student Package ---")

    name = input("Enter student name: ")

    m1 = float(input("Enter marks 1: "))
    m2 = float(input("Enter marks 2: "))
    m3 = float(input("Enter marks 3: "))

    attendance = float(input("Enter attendance percentage: "))

    total = m1 + m2 + m3
    percentage = total / 3

    if percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    else:
        grade = "D"

    print("\nStudent:", name)
    print("Total:", total)
    print("Percentage:", percentage)
    print("Grade:", grade)

    if attendance >= 75:
        print("Attendance: Eligible")
    else:
        print("Attendance: Not Eligible")


# 24. Texttools Package
def package_3_texttools():
    print("\n--- Texttools Package ---")

    text = input("Enter text: ")

    # Cleaning
    clean_text = ""

    for ch in text:
        if ch not in string.punctuation:
            clean_text += ch

    clean_text = " ".join(clean_text.split())

    print("Cleaned text:", clean_text)

    # Tokenization
    words = clean_text.split()

    print("Tokens:", words)

    # Frequency
    frequency = {}

    for word in words:
        word = word.lower()

        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    print("Word Frequency:")

    for word, count in frequency.items():
        print(word, ":", count)


# ============================================================
#                     DIRECTORY PROGRAMS
# ============================================================

# 25. College Project Directory
def directory_1_college():
    print("\n--- College Project Directory ---")

    print("\nStudent Details")
    student_name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    branch = input("Enter branch: ")

    print("\nFaculty Details")
    faculty_name = input("Enter faculty name: ")
    subject = input("Enter subject: ")

    print("\n===== COLLEGE PROJECT =====")
    print("Student Name:", student_name)
    print("Roll Number:", roll)
    print("Branch:", branch)

    print("\nFaculty Name:", faculty_name)
    print("Subject:", subject)


# 26. Library Application Directory
def directory_2_library():
    print("\n--- Library Application Directory ---")

    book = input("Enter book name: ")
    author = input("Enter author name: ")
    member = input("Enter member name: ")

    print("\n===== LIBRARY DETAILS =====")
    print("Book:", book)
    print("Author:", author)
    print("Member:", member)

    choice = input("Enter 1 to Issue or 2 to Return: ")

    if choice == "1":
        print("Book issued successfully.")
    elif choice == "2":
        print("Book returned successfully.")
    else:
        print("Invalid choice.")


# ============================================================
#                         MAIN MENU
# ============================================================

def main():

    while True:

        print("\n")
        print("=" * 55)
        print("          PYTHON PRACTICAL PROGRAMS")
        print("=" * 55)

        print("\n--- FILE HANDLING PROGRAMS ---")
        print("1.  Create and write student file")
        print("2.  Display complete file")
        print("3.  Append information")
        print("4.  Read file line by line")
        print("5.  Count total lines")
        print("6.  Count total words")
        print("7.  Count total characters")
        print("8.  Display lines in reverse")
        print("9.  Count vowels and consonants")
        print("10. Count alphabets, digits, spaces and special characters")
        print("11. Find longest word")
        print("12. Count each word")
        print("13. Search word and show line numbers")
        print("14. Replace word")
        print("15. Remove Python comments")
        print("16. Create uppercase copy")

        print("\n--- MODULE PROGRAMS ---")
        print("17. Calculator Module")
        print("18. Student Result Module")
        print("19. Number Utilities Module")
        print("20. String Utilities Module")
        print("21. Recursive Functions Module")

        print("\n--- PACKAGE PROGRAMS ---")
        print("22. Mathutils Package")
        print("23. Student Package")
        print("24. Texttools Package")

        print("\n--- DIRECTORY PROGRAMS ---")
        print("25. College Project Directory")
        print("26. Library Application Directory")

        print("\n0. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            file_program_1()
        elif choice == "2":
            file_program_2()
        elif choice == "3":
            file_program_3()
        elif choice == "4":
            file_program_4()
        elif choice == "5":
            file_program_5()
        elif choice == "6":
            file_program_6()
        elif choice == "7":
            file_program_7()
        elif choice == "8":
            file_program_8()
        elif choice == "9":
            file_program_9()
        elif choice == "10":
            file_program_10()
        elif choice == "11":
            file_program_11()
        elif choice == "12":
            file_program_12()
        elif choice == "13":
            file_program_13()
        elif choice == "14":
            file_program_14()
        elif choice == "15":
            file_program_15()
        elif choice == "16":
            file_program_16()

        elif choice == "17":
            module_1_calculator()
        elif choice == "18":
            module_2_student()
        elif choice == "19":
            module_3_numbers()
        elif choice == "20":
            module_4_strings()
        elif choice == "21":
            module_5_recursive()

        elif choice == "22":
            package_1_mathutils()
        elif choice == "23":
            package_2_student()
        elif choice == "24":
            package_3_texttools()

        elif choice == "25":
            directory_1_college()
        elif choice == "26":
            directory_2_library()

        elif choice == "0":
            print("Program ended.")
            break

        else:
            print("Invalid choice. Please try again.")


# Start program
main()