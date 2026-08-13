


# 1. Create a set containing five integers
print("\n1. Set of Five Integers")

numbers = {10, 20, 30, 40, 50}

print("Set:", numbers)


# 2. Convert list with duplicates into a set
print("\n2. Remove Duplicates Using Set")

numbers = [10, 20, 10, 30, 20, 40, 30, 50]

numbers_set = set(numbers)

print("Original list:", numbers)
print("Set:", numbers_set)


# 3. Add two new fruits
print("\n3. Add Fruits to Set")

fruits = {"Apple", "Banana", "Mango", "Orange", "Grapes"}

fruits.add("Pineapple")
fruits.add("Watermelon")

print("Updated set:", fruits)


# 4. Remove specified number
print("\n4. Remove Number from Set")

numbers = {10, 20, 30, 40, 50}

num = int(input("Enter number to remove: "))

if num in numbers:
    numbers.remove(num)
    print("Updated set:", numbers)
else:
    print("Number not found.")


# 5. Check whether student exists
print("\n5. Check Student Name")

students = {"Amit", "Rahul", "Sneha", "Priya", "Riya"}

name = input("Enter student name: ")

if name in students:
    print("Student exists in the set.")
else:
    print("Student does not exist.")


# 6. Count total number of cities
print("\n6. Number of Cities")

cities = {"Mumbai", "Pune", "Delhi", "Nashik", "Sangli"}

print("Cities:", cities)
print("Total cities:", len(cities))


# 7. Display programming languages using loop
print("\n7. Programming Languages")

languages = {"Python", "Java", "C", "C++", "JavaScript"}

for language in languages:
    print(language)


# 8. Remove duplicate numbers using set
print("\n8. Remove Duplicate Numbers")

numbers = [1, 2, 3, 2, 4, 1, 5, 3, 6]

unique_numbers = set(numbers)

print("Original list:", numbers)
print("After removing duplicates:", unique_numbers)


# 9. Union of two sets
print("\n9. Union of Two Sets")

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

union_set = set1.union(set2)

print("Set 1:", set1)
print("Set 2:", set2)
print("Union:", union_set)


# 10. Common elements of two sets
print("\n10. Intersection of Two Sets")

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

common = set1.intersection(set2)

print("Common elements:", common)


# 11. Difference between two sets
print("\n11. Difference of Two Sets")

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

first_only = set1 - set2
second_only = set2 - set1

print("First set but not second:", first_only)
print("Second set but not first:", second_only)


# 12. Elements in either set but not both
print("\n12. Symmetric Difference")

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

result = set1.symmetric_difference(set2)

print("Elements in either set but not both:", result)


# 13. Check subset
print("\n13. Check Subset")

set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}

if set1.issubset(set2):
    print("First set is a subset of second set.")
else:
    print("First set is not a subset of second set.")


# 14. Check superset
print("\n14. Check Superset")

set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3}

if set1.issuperset(set2):
    print("First set is a superset of second set.")
else:
    print("First set is not a superset of second set.")


# 15. Check whether sets are disjoint
print("\n15. Check Disjoint Sets")

set1 = {1, 2, 3}
set2 = {4, 5, 6}

if set1.isdisjoint(set2):
    print("Sets have no elements in common.")
else:
    print("Sets have elements in common.")


# 16. Check whether two sets are equal
print("\n16. Check Equal Sets")

set1 = {1, 2, 3, 4}
set2 = {4, 3, 2, 1}

if set1 == set2:
    print("Both sets are equal.")
else:
    print("Sets are not equal.")


# 17. Subjects studied by both students
print("\n17. Common Subjects")

student1 = {"Python", "Java", "DBMS", "CN"}
student2 = {"Java", "Python", "OS", "Maths"}

common_subjects = student1.intersection(student2)

print("Subjects studied by both:", common_subjects)


# 18. Unique words from a sentence
print("\n18. Unique Words")

sentence = input("Enter a sentence: ")

words = sentence.split()

unique_words = set(words)

print("Unique words:", unique_words)


# 19. Morning and afternoon session students
print("\n19. Morning and Afternoon Sessions")

morning = {"Amit", "Rahul", "Sneha", "Priya", "Riya"}
afternoon = {"Sneha", "Priya", "Karan", "Neha", "Riya"}

both_sessions = morning.intersection(afternoon)
morning_only = morning - afternoon
afternoon_only = afternoon - morning
at_least_one = morning.union(afternoon)

print("Students in both sessions:", both_sessions)
print("Only morning:", morning_only)
print("Only afternoon:", afternoon_only)
print("At least one session:", at_least_one)


# 20. Students enrolled in Python and Java
print("\n20. Python and Java Students")

python_students = {"Amit", "Rahul", "Sneha", "Priya"}
java_students = {"Sneha", "Priya", "Riya", "Karan"}

print("Python students:", python_students)
print("Java students:", java_students)


# 21. Students in both courses and only one course
print("\n21. Common and Unique Course Students")

python_students = {"Amit", "Rahul", "Sneha", "Priya"}
java_students = {"Sneha", "Priya", "Riya", "Karan"}

both_courses = python_students.intersection(java_students)
only_one_course = python_students.symmetric_difference(java_students)

print("Students in both courses:", both_courses)
print("Students in only one course:", only_one_course)


# 22. Technical skills of two employees
print("\n22. Employee Technical Skills")

employee1 = {"Python", "Java", "SQL", "Git"}
employee2 = {"Python", "JavaScript", "SQL", "Docker"}

common_skills = employee1.intersection(employee2)
unique_employee1 = employee1 - employee2
unique_employee2 = employee2 - employee1
all_skills = employee1.union(employee2)

print("Common skills:", common_skills)
print("Skills unique to Employee 1:", unique_employee1)
print("Skills unique to Employee 2:", unique_employee2)
print("All available skills:", all_skills)


# 23. Available and requested books
print("\n23. Available Books")

available_books = {
    "Python Basics",
    "Java Programming",
    "Data Structures",
    "DBMS",
    "Computer Networks"
}

requested_books = {
    "Python Basics",
    "DBMS",
    "Machine Learning",
    "Data Structures"
}

available_requested = requested_books.intersection(available_books)

print("Requested books:", requested_books)
print("Books that are available:", available_requested)


# 24. Visitors on two different days
print("\n24. Visitors on Two Days")

day1 = {101, 102, 103, 104, 105}
day2 = {103, 104, 105, 106, 107}

unique_visitors = day1.union(day2)
returning_visitors = day1.intersection(day2)
first_day_only = day1 - day2
second_day_only = day2 - day1

print("Unique visitors:", unique_visitors)
print("Returning visitors:", returning_visitors)
print("Visitors only on first day:", first_day_only)
print("Visitors only on second day:", second_day_only)


# 25. Products belonging to different categories
print("\n25. Products in Both Categories")

electronics = {
    "Laptop",
    "Mobile",
    "Tablet",
    "Headphones",
    "Smartwatch"
}

gadgets = {
    "Mobile",
    "Smartwatch",
    "Camera",
    "Headphones",
    "Speaker"
}

common_products = electronics.intersection(gadgets)

print("Electronics:", electronics)
print("Gadgets:", gadgets)
print("Products belonging to both categories:", common_products)