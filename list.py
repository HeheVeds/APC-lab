


# 1. Create a list of five fruits
print("\n1. List of Five Fruits")

fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

print("Fruits:", fruits)


# 2. Display first, last and third element
print("\n2. List Elements")

numbers = [10, 20, 30, 40, 50]

print("First element:", numbers[0])
print("Last element:", numbers[-1])
print("Third element:", numbers[2])


# 3. Replace third color
print("\n3. Replace Third Color")

colors = ["Red", "Blue", "Green", "Yellow", "Black"]

colors[2] = "Pink"

print("Updated list:", colors)


# 4. Add elements at end, beginning and specified position
print("\n4. Add Elements")

numbers = [10, 20, 30, 40]

numbers.append(50)       # End
numbers.insert(0, 5)     # Beginning
numbers.insert(3, 25)    # Specified position

print("Updated list:", numbers)


# 5. Remove first, last and specific student
print("\n5. Remove Students")

students = ["Amit", "Rahul", "Sneha", "Priya", "Riya"]

students.pop(0)          # First student
students.pop()           # Last student

if "Sneha" in students:
    students.remove("Sneha")

print("Remaining students:", students)


# 6. Largest and smallest without max() and min()
print("\n6. Largest and Smallest")

numbers = [45, 12, 78, 34, 90, 23]

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

print("Largest:", largest)
print("Smallest:", smallest)


# 7. Accept 10 numbers and calculate sum and average
print("\n7. Sum and Average")

numbers = []

for i in range(10):
    num = int(input("Enter number: "))
    numbers.append(num)

total = sum(numbers)
average = total / len(numbers)

print("Numbers:", numbers)
print("Sum:", total)
print("Average:", average)


# 8. Count even and odd numbers
print("\n8. Even and Odd Count")

numbers = [
    1, 2, 3, 4, 5,
    6, 7, 8, 9, 10,
    11, 12, 13, 14, 15
]

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even numbers:", even_count)
print("Odd numbers:", odd_count)


# 9. Search city in list
print("\n9. Search City")

cities = ["Mumbai", "Pune", "Kolhapur", "Sangli", "Nashik"]

city = input("Enter city name: ")

if city in cities:
    print("City exists in the list.")
else:
    print("City does not exist.")


# 10. Reverse list without reverse()
print("\n10. Reverse List")

numbers = [10, 20, 30, 40, 50]

reversed_list = []

for i in range(len(numbers) - 1, -1, -1):
    reversed_list.append(numbers[i])

print("Original list:", numbers)
print("Reversed list:", reversed_list)


# 11. List slicing
print("\n11. List Slicing")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("First 5 elements:", numbers[:5])
print("Last 5 elements:", numbers[-5:])
print("Middle 4 elements:", numbers[3:7])
print("Alternate elements:", numbers[::2])
print("Reverse list:", numbers[::-1])


# 12. Elements at even index positions
print("\n12. Elements at Even Index Positions")

numbers = [10, 20, 30, 40, 50, 60, 70, 80]

for i in range(0, len(numbers), 2):
    print(numbers[i])


# 13. Sort 10 numbers ascending and descending
print("\n13. Sorting")

numbers = []

for i in range(10):
    num = int(input("Enter number: "))
    numbers.append(num)

ascending = sorted(numbers)
descending = sorted(numbers, reverse=True)

print("Original list:", numbers)
print("Ascending order:", ascending)
print("Descending order:", descending)


# 14. Display only unique elements
print("\n14. Unique Elements")

numbers = [10, 20, 10, 30, 20, 40, 30, 50]

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print("Original list:", numbers)
print("Unique elements:", unique)


# 15. Find second largest element
print("\n15. Second Largest Element")

numbers = [10, 50, 30, 90, 70, 90]

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

unique.sort()

if len(unique) >= 2:
    print("Second largest:", unique[-2])
else:
    print("Second largest element does not exist.")


# 16. Nested list for student details
print("\n16. Nested Student List")

students = [
    ["Amit", 101, 85],
    ["Rahul", 102, 78],
    ["Sneha", 103, 92]
]

for student in students:
    print("Name:", student[0])
    print("Roll Number:", student[1])
    print("Marks:", student[2])
    print()


# 17. Matrix addition of two 3x3 matrices
print("\n17. Matrix Addition")

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

result = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for i in range(3):
    for j in range(3):
        result[i][j] = matrix1[i][j] + matrix2[i][j]

print("Result matrix:")

for row in result:
    print(row)


# 18. Shopping cart
print("\n18. Shopping Cart")

cart = []

# Add item
item = input("Enter item to add: ")
cart.append(item)

# Add another item
item = input("Enter another item to add: ")
cart.append(item)

# Display cart
print("Cart:", cart)

# Search item
search = input("Enter item to search: ")

if search in cart:
    print("Item found.")
else:
    print("Item not found.")

# Remove item
remove = input("Enter item to remove: ")

if remove in cart:
    cart.remove(remove)
    print("Item removed.")
else:
    print("Item not found.")

print("Final cart:", cart)
print("Total items:", len(cart))


# 19. Student attendance list
print("\n19. Student Attendance")

students = ["Amit", "Rahul", "Sneha", "Priya"]

print("Total students:", len(students))

name = input("Enter student name to search: ")

if name in students:
    print("Student is present.")
else:
    print("Student is absent.")

new_student = input("Enter new student name: ")
students.append(new_student)

absent_student = input("Enter absent student name to remove: ")

if absent_student in students:
    students.remove(absent_student)

print("Final student list:", students)
print("Total students:", len(students))


# 20. Book list
print("\n20. Book Management")

books = ["Python Basics", "Java Programming", "DBMS", "Data Structures"]

# Add
new_book = input("Enter book to add: ")
books.append(new_book)

# Search
search_book = input("Enter book to search: ")

if search_book in books:
    print("Book found.")
else:
    print("Book not found.")

# Remove
remove_book = input("Enter book to remove: ")

if remove_book in books:
    books.remove(remove_book)
    print("Book removed.")
else:
    print("Book not found.")

# Display and count
print("All books:", books)
print("Total books:", len(books))


# 21. Merge two lists
print("\n21. Merge Two Lists")

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

merged = list1 + list2

print("List 1:", list1)
print("List 2:", list2)
print("Merged list:", merged)


# 22. Common elements between two lists
print("\n22. Common Elements")

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

common = []

for item in list1:
    if item in list2 and item not in common:
        common.append(item)

print("Common elements:", common)


# 23. Frequency of each element
print("\n23. Element Frequency")

numbers = [1, 2, 2, 3, 1, 4, 2, 3, 5, 1]

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print("Frequency:", frequency)


# 24. Rotate list left and right by one position
print("\n24. Rotate List")

numbers = [1, 2, 3, 4, 5]

left = numbers[1:] + numbers[:1]
right = numbers[-1:] + numbers[:-1]

print("Original list:", numbers)
print("Left rotation:", left)
print("Right rotation:", right)


# 25. Remove duplicates while preserving order
print("\n25. Remove Duplicates")

numbers = [1, 2, 3, 2, 4, 1, 5, 3, 6]

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print("Original list:", numbers)
print("Without duplicates:", unique)


# 26. Marks of 20 students
print("\n26. Student Marks Analysis")

marks = [
    78, 85, 92, 67, 88,
    95, 72, 81, 90, 76,
    84, 69, 91, 73, 87,
    80, 66, 94, 89, 75
]

highest = marks[0]
lowest = marks[0]

for mark in marks:
    if mark > highest:
        highest = mark

    if mark < lowest:
        lowest = mark

total = sum(marks)
average = total / len(marks)

above_average = 0
below_average = 0

for mark in marks:
    if mark > average:
        above_average += 1
    elif mark < average:
        below_average += 1

print("Highest marks:", highest)
print("Lowest marks:", lowest)
print("Average marks:", average)
print("Students above average:", above_average)
print("Students below average:", below_average)


# 27. Employee salaries
print("\n27. Employee Salary Analysis")

salaries = [
    25000, 35000, 55000, 70000, 45000,
    60000, 28000, 80000, 52000, 30000
]

highest = salaries[0]
lowest = salaries[0]

for salary in salaries:
    if salary > highest:
        highest = salary

    if salary < lowest:
        lowest = salary

total = sum(salaries)
average = total / len(salaries)

above_50000 = 0
below_30000 = 0

for salary in salaries:
    if salary > 50000:
        above_50000 += 1

    if salary < 30000:
        below_30000 += 1

print("Highest salary: ₹", highest)
print("Lowest salary: ₹", lowest)
print("Average salary: ₹", average)
print("Employees earning above ₹50,000:", above_50000)
print("Employees earning below ₹30,000:", below_30000)


# 28. Batsman scores in 10 matches
print("\n28. Batsman Score Analysis")

scores = [45, 102, 67, 120, 34, 89, 55, 150, 42, 78]

highest = scores[0]
lowest = scores[0]

for score in scores:
    if score > highest:
        highest = score

    if score < lowest:
        lowest = score

total_runs = sum(scores)
average = total_runs / len(scores)

centuries = 0
half_centuries = 0

for score in scores:
    if score >= 100:
        centuries += 1
    elif score >= 50:
        half_centuries += 1

print("Highest score:", highest)
print("Lowest score:", lowest)
print("Total runs:", total_runs)
print("Average runs:", average)
print("Centuries:", centuries)
print("Half-centuries:", half_centuries)


# 29. Temperature of 30 days
print("\n29. Temperature Analysis")

temperatures = [
    25, 28, 30, 32, 29,
    27, 31, 35, 33, 30,
    26, 24, 29, 34, 36,
    31, 28, 27, 32, 30,
    29, 35, 37, 33, 31,
    26, 25, 34, 36, 32
]

hottest = temperatures[0]
coldest = temperatures[0]

for temp in temperatures:
    if temp > hottest:
        hottest = temp

    if temp < coldest:
        coldest = temp

total = sum(temperatures)
average = total / len(temperatures)

above_average = 0
below_average = 0

for temp in temperatures:
    if temp > average:
        above_average += 1
    elif temp < average:
        below_average += 1

print("Hottest temperature:", hottest)
print("Coldest temperature:", coldest)
print("Average temperature:", average)
print("Days above average:", above_average)
print("Days below average:", below_average)


# 30. Patient management using lists
print("\n30. Patient Management")

patient_names = ["Amit", "Rahul", "Sneha", "Priya"]
patient_ages = [25, 30, 22, 35]

# Add a patient
new_name = input("Enter new patient name: ")
new_age = int(input("Enter patient age: "))

patient_names.append(new_name)
patient_ages.append(new_age)

# Search a patient
search_name = input("Enter patient name to search: ")

if search_name in patient_names:
    index = patient_names.index(search_name)
    print("Patient found.")
    print("Name:", patient_names[index])
    print("Age:", patient_ages[index])
else:
    print("Patient not found.")

# Delete a patient
delete_name = input("Enter patient name to delete: ")

if delete_name in patient_names:
    index = patient_names.index(delete_name)

    patient_names.pop(index)
    patient_ages.pop(index)

    print("Patient deleted.")
else:
    print("Patient not found.")

# Display all patients
print("\nAll Patients:")

for i in range(len(patient_names)):
    print("Name:", patient_names[i], "Age:", patient_ages[i])

# Count patients
print("Total patients:", len(patient_names))