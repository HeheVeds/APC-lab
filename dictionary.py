

# 1. Student details and display all key-value pairs
print("\n1. Student Details")

student = {
    "roll_no": 101,
    "name": "Vedika",
    "department": "CSE",
    "marks": 85
}

for key, value in student.items():
    print(key, ":", value)


# 2. Employee information and display value of specified key
print("\n2. Employee Information")

employee = {
    "name": "Rahul",
    "age": 25,
    "department": "IT",
    "salary": 50000
}

key = input("Enter key to display value: ")

if key in employee:
    print("Value:", employee[key])
else:
    print("Key not found.")


# 3. Five products and prices, add new product
print("\n3. Products and Prices")

products = {
    "Laptop": 50000,
    "Mobile": 20000,
    "Mouse": 500,
    "Keyboard": 1000,
    "Headphones": 1500
}

print("Original dictionary:", products)

products["Printer"] = 8000

print("After adding new product:", products)


# 4. Student marks and update specified student's marks
print("\n4. Update Student Marks")

marks = {
    "Amit": 75,
    "Rahul": 82,
    "Sneha": 90,
    "Priya": 88
}

name = input("Enter student name: ")

if name in marks:
    new_marks = int(input("Enter new marks: "))
    marks[name] = new_marks
    print("Updated dictionary:", marks)
else:
    print("Student not found.")


# 5. Cities and populations, remove specified city
print("\n5. Remove City")

cities = {
    "Mumbai": 20000000,
    "Pune": 7000000,
    "Delhi": 19000000,
    "Nashik": 1800000
}

print("Original dictionary:", cities)

city = input("Enter city to remove: ")

if city in cities:
    del cities[city]
    print("Updated dictionary:", cities)
else:
    print("City not found.")


# 6. Employee IDs and names, check whether ID exists
print("\n6. Search Employee ID")

employees = {
    101: "Amit",
    102: "Rahul",
    103: "Sneha",
    104: "Priya",
    105: "Riya"
}

emp_id = int(input("Enter employee ID: "))

if emp_id in employees:
    print("Employee ID exists.")
    print("Employee name:", employees[emp_id])
else:
    print("Employee ID does not exist.")


# 7. Student records and total number of key-value pairs
print("\n7. Number of Key-Value Pairs")

students = {
    "Amit": 80,
    "Rahul": 75,
    "Sneha": 90,
    "Priya": 85
}

print("Dictionary:", students)
print("Total key-value pairs:", len(students))


# 8. Display all keys, values and key-value pairs
print("\n8. Keys, Values and Key-Value Pairs")

data = {
    "Name": "Vedika",
    "Age": 20,
    "Department": "CSE",
    "Marks": 85
}

print("All Keys:")
print(data.keys())

print("All Values:")
print(data.values())

print("All Key-Value Pairs:")
print(data.items())


# 9. Programming languages and creators
print("\n9. Programming Languages and Creators")

languages = {
    "Python": "Guido van Rossum",
    "C": "Dennis Ritchie",
    "Java": "James Gosling",
    "C++": "Bjarne Stroustrup"
}

for language, creator in languages.items():
    print(language, ":", creator)


# 10. Accept five student names and marks
print("\n10. Student Names and Marks")

students = {}

for i in range(5):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

print("Student dictionary:", students)


# 11. Student with highest marks
print("\n11. Student with Highest Marks")

marks = {
    "Amit": 75,
    "Rahul": 92,
    "Sneha": 88,
    "Priya": 95,
    "Riya": 81
}

highest_student = ""
highest_marks = 0

for name, mark in marks.items():
    if mark > highest_marks:
        highest_marks = mark
        highest_student = name

print("Highest scorer:", highest_student)
print("Marks:", highest_marks)


# 12. Student with lowest marks
print("\n12. Student with Lowest Marks")

marks = {
    "Amit": 75,
    "Rahul": 92,
    "Sneha": 88,
    "Priya": 95,
    "Riya": 81
}

lowest_student = ""
lowest_marks = 101

for name, mark in marks.items():
    if mark < lowest_marks:
        lowest_marks = mark
        lowest_student = name

print("Lowest scorer:", lowest_student)
print("Marks:", lowest_marks)


# 13. Average marks of all students
print("\n13. Average Marks")

marks = {
    "Amit": 75,
    "Rahul": 92,
    "Sneha": 88,
    "Priya": 95,
    "Riya": 81
}

total = 0

for mark in marks.values():
    total = total + mark

average = total / len(marks)

print("Average marks:", average)


# 14. Character frequency in a string
print("\n14. Character Frequency")

text = input("Enter a string: ")

frequency = {}

for char in text:
    if char in frequency:
        frequency[char] = frequency[char] + 1
    else:
        frequency[char] = 1

print("Character frequency:", frequency)


# 15. Word frequency in a sentence
print("\n15. Word Frequency")

sentence = input("Enter a sentence: ")

words = sentence.split()

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] = frequency[word] + 1
    else:
        frequency[word] = 1

print("Word frequency:", frequency)


# 16. Merge two dictionaries
print("\n16. Merge Two Dictionaries")

dict1 = {
    "a": 10,
    "b": 20,
    "c": 30
}

dict2 = {
    "d": 40,
    "e": 50,
    "f": 60
}

merged = dict1.copy()
merged.update(dict2)

print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)
print("Merged dictionary:", merged)


# 17. Common keys in two dictionaries
print("\n17. Common Keys")

dict1 = {
    "a": 10,
    "b": 20,
    "c": 30,
    "d": 40
}

dict2 = {
    "b": 50,
    "c": 60,
    "e": 70,
    "f": 80
}

common_keys = []

for key in dict1:
    if key in dict2:
        common_keys.append(key)

print("Common keys:", common_keys)


# 18. Common values in two dictionaries
print("\n18. Common Values")

dict1 = {
    "a": 10,
    "b": 20,
    "c": 30
}

dict2 = {
    "x": 20,
    "y": 40,
    "z": 30
}

common_values = []

for value in dict1.values():
    if value in dict2.values() and value not in common_values:
        common_values.append(value)

print("Common values:", common_values)


# 19. Remove duplicate values while retaining keys
print("\n19. Remove Duplicate Values")

data = {
    "A": 10,
    "B": 20,
    "C": 10,
    "D": 30,
    "E": 20
}

new_dict = {}

for key, value in data.items():
    if value not in new_dict.values():
        new_dict[key] = value

print("Original dictionary:", data)
print("After removing duplicate values:", new_dict)


# 20. Display dictionary in ascending order of keys
print("\n20. Dictionary in Ascending Order of Keys")

data = {
    5: "E",
    2: "B",
    4: "D",
    1: "A",
    3: "C"
}

sorted_dict = {}

for key in sorted(data):
    sorted_dict[key] = data[key]

print("Original dictionary:", data)
print("Sorted dictionary:", sorted_dict)


# 21. Numbers 1 to 10 and their squares
print("\n21. Squares from 1 to 10")

squares = {}

for num in range(1, 11):
    squares[num] = num * num

print(squares)


# 22. Even numbers from 1 to 20 and their squares
print("\n22. Squares of Even Numbers from 1 to 20")

even_squares = {}

for num in range(1, 21):
    if num % 2 == 0:
        even_squares[num] = num * num

print(even_squares)


# 23. Frequency of unique numbers in a list
print("\n23. Frequency of Numbers")

numbers = [1, 2, 3, 2, 4, 1, 2, 5, 3, 4, 1]

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] = frequency[num] + 1
    else:
        frequency[num] = 1

print("List:", numbers)
print("Frequency:", frequency)