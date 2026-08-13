

# 1. Create a tuple of five integers and display it
print("\n1. Tuple of five integers")

numbers = (10, 20, 30, 40, 50)
print("Tuple:", numbers)


# 2. Tuple of five city names
print("\n2. First, Last and Third City")

cities = ("Mumbai", "Pune", "Kolhapur", "Sangli", "Nashik")

print("First city:", cities[0])
print("Last city:", cities[-1])
print("Third city:", cities[2])


# 3. Tuple of student names and display total number
print("\n3. Number of Students")

students = ("Amit", "Rahul", "Sneha", "Priya", "Riya")

print("Students:", students)
print("Total students:", len(students))


# 4. Check whether a color exists in tuple
print("\n4. Check Color")

colors = ("Red", "Blue", "Green", "Yellow", "Black")

color = input("Enter a color to search: ")

if color in colors:
    print("Color exists in the tuple.")
else:
    print("Color does not exist in the tuple.")


# 5. Display each fruit using a loop
print("\n5. Fruits")

fruits = ("Apple", "Banana", "Mango", "Orange", "Grapes")

for fruit in fruits:
    print(fruit)


# 6. Count repeated number
print("\n6. Count Occurrence of Number")

numbers = (10, 20, 10, 30, 10, 40, 20, 10)

num = int(input("Enter number to count: "))

count = numbers.count(num)

print("Number of times", num, "appears:", count)


# 7. Find index of employee ID
print("\n7. Employee ID Index")

employee_ids = (101, 102, 103, 104, 105)

emp_id = int(input("Enter employee ID: "))

if emp_id in employee_ids:
    print("Index:", employee_ids.index(emp_id))
else:
    print("Employee ID not found.")


# 8. Concatenate two tuples
print("\n8. Concatenate Two Tuples")

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

result = tuple1 + tuple2

print("First tuple:", tuple1)
print("Second tuple:", tuple2)
print("Concatenated tuple:", result)


# 9. Repeat tuple four times
print("\n9. Repeat Tuple Four Times")

my_tuple = (1, 2, 3)

result = my_tuple * 4

print("Original tuple:", my_tuple)
print("Repeated tuple:", result)


# 10. Tuple slicing
print("\n10. Tuple Slicing")

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print("Tuple:", numbers)

print("First five elements:", numbers[:5])
print("Last five elements:", numbers[-5:])
print("Middle four elements:", numbers[3:7])
print("Alternate elements:", numbers[::2])
print("Reverse tuple:", numbers[::-1])


# 11. Convert tuple into list and add new element
print("\n11. Tuple to List")

fruits = ("Apple", "Banana", "Mango")

fruit_list = list(fruits)
fruit_list.append("Orange")

print("Original tuple:", fruits)
print("List after adding element:", fruit_list)


# 12. Accept five numbers, store in list and convert to tuple
print("\n12. List to Tuple")

numbers = []

for i in range(5):
    num = int(input("Enter number: "))
    numbers.append(num)

numbers_tuple = tuple(numbers)

print("List:", numbers)
print("Tuple:", numbers_tuple)


# 13. Modify tuple by converting to list
print("\n13. Modify a Tuple")

numbers = (10, 20, 30, 40)

print("Original tuple:", numbers)

numbers_list = list(numbers)

numbers_list[1] = 25

numbers = tuple(numbers_list)

print("Modified tuple:", numbers)


# 14. Create and delete tuple completely
print("\n14. Delete Tuple")

my_tuple = (10, 20, 30, 40)

print("Tuple before deletion:", my_tuple)

del my_tuple

print("Tuple deleted successfully.")


# 15. Nested tuple containing student details
print("\n15. Nested Tuple")

students = (
    (101, "Amit", "CSE", 85),
    (102, "Sneha", "IT", 90),
    (103, "Rahul", "CSE", 78)
)

for student in students:
    print(student)


# 16. Sum of ten numbers
print("\n16. Sum of Tuple Elements")

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

total = sum(numbers)

print("Tuple:", numbers)
print("Sum:", total)


# 17. Largest and smallest without max() and min()
print("\n17. Largest and Smallest Number")

numbers = (45, 12, 78, 34, 90, 23)

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

print("Tuple:", numbers)
print("Largest:", largest)
print("Smallest:", smallest)


# 18. Average of tuple elements
print("\n18. Average of Tuple")

numbers = (10, 20, 30, 40, 50)

total = sum(numbers)
average = total / len(numbers)

print("Tuple:", numbers)
print("Average:", average)


# 19. Count even and odd numbers
print("\n19. Count Even and Odd Numbers")

numbers = (
    1, 2, 3, 4, 5,
    6, 7, 8, 9, 10,
    11, 12, 13, 14, 15
)

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Tuple:", numbers)
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)


# 20. Accept number and check whether it exists
print("\n20. Search Number in Tuple")

numbers = (10, 20, 30, 40, 50)

num = int(input("Enter a number to search: "))

if num in numbers:
    print("Number exists in the tuple.")
else:
    print("Number does not exist in the tuple.")


# 21. Student details in a tuple
print("\n21. Student Details")

student = (101, "Vedika", "CSE", 85)

print("Roll Number:", student[0])
print("Name:", student[1])
print("Department:", student[2])
print("Marks:", student[3])