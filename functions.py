

# 1. Write a function factorial(n) that accepts an integer and returns its factorial.
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

# 2. Write a function check_even_odd(n) that determines whether a given number is even or odd.
def check_even_odd(n):
    return "Even" if n % 2 == 0 else "Odd"

# 3. Define a function that accepts two numbers and returns the greater number.
def get_greater(a, b):
    return a if a > b else b

# 4. Create a function simple_interest(p, r, t) to calculate simple interest.
def simple_interest(p, r, t):
    return (p * r * t) / 100

# 5. Write a function is_prime(n) that returns True if a number is prime.
def is_prime(n):
    if n <= 1: return False
    # Using n ** 0.5 instead of math.sqrt
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: return False
    return True

# 6. Define a function to calculate the area of a circle using its radius.
def area_of_circle(radius):
    pi = 3.141592653589793
    return pi * (radius ** 2)

# 7. Write a function that accepts n and returns the sum of the first n natural numbers.
def sum_of_natural_numbers(n):
    return n * (n + 1) // 2

# 8. Create a function power(base, exponent) to calculate the value of base raised to exponent.
def power(base, exponent):
    return base ** exponent



# 9. Return the largest element without using the built-in max() function.
def find_largest(lst):
    if not lst: return None
    largest = lst[0]
    for num in lst:
        if num > largest: largest = num
    return largest

# 10. Accept a string and return the number of vowels present in it.
def count_vowels(s):
    return sum(1 for char in s.lower() if char in 'aeiou')

# 11. Accept a string and return its reverse.
def reverse_string(s):
    return s[::-1]

# 12. Check whether a given string or number is a palindrome.
def is_palindrome(val):
    s = str(val)
    return s == s[::-1]

# 13. Accept a list of numbers and return their average.
def average_list(lst):
    return sum(lst) / len(lst) if lst else 0

# 14. Accept a list and an element and return the number of times that element occurs.
def count_occurrences(lst, element):
    return lst.count(element)

# 15. Accept a list and return a new list containing only unique elements.
def get_unique(lst):
    return list(set(lst))

# 16. Find the second-largest number in a list.
def second_largest(lst):
    unique_lst = list(set(lst))
    unique_lst.sort(reverse=True)
    return unique_lst[1] if len(unique_lst) > 1 else None

# 17. Accept n and return the first n Fibonacci numbers.
def fibonacci(n):
    if n <= 0: return []
    if n == 1: return [0]
    fib = [0, 1]
    for _ in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

# 22. Accept a list of numbers and return the minimum, maximum, sum, and average.
def list_stats(lst):
    if not lst: return None
    return min(lst), max(lst), sum(lst), sum(lst)/len(lst)



# 18. Accept marks in five subjects and return the student's percentage and grade.
def student_result(marks):
    percentage = sum(marks) / len(marks)
    if percentage >= 90: grade = 'A'
    elif percentage >= 75: grade = 'B'
    elif percentage >= 50: grade = 'C'
    else: grade = 'F'
    return percentage, grade

# 19. Accept units consumed and calculate the electricity bill according to predefined slabs.
def electricity_bill_basic(units):
    if units <= 100: return units * 5
    elif units <= 200: return (100 * 5) + ((units - 100) * 7)
    else: return (100 * 5) + (100 * 7) + ((units - 200) * 10)

# 20. Accept basic salary and calculate gross salary after adding HRA and DA.
def gross_salary(basic):
    hra = basic * 0.20
    da = basic * 0.50
    return basic + hra + da

# 21. Accept item prices and quantities and return the total bill after applying a discount.
def shopping_bill(prices, quantities, discount_percent):
    total = sum(p * q for p, q in zip(prices, quantities))
    return total - (total * (discount_percent / 100))




# 29. Recursive binary search for an element in a sorted list.
def binary_search(lst, target, low, high):
    if low > high: return -1
    mid = (low + high) // 2
    if lst[mid] == target: return mid
    elif lst[mid] > target: return binary_search(lst, target, low, mid - 1)
    else: return binary_search(lst, target, mid + 1, high)

# 30. Convert a decimal number into binary using recursion.
def decimal_to_binary(n):
    if n == 0: return ""
    if n == 1: return "1"
    return decimal_to_binary(n // 2) + str(n % 2)


# 33. Lambda function to calculate the square of a given number.
square = lambda x: x ** 2

# 34. Lambda function that returns the cube of a number.
cube = lambda x: x ** 3

# 35. Lambda function that returns True if a number is even and False otherwise.
is_even = lambda x: x % 2 == 0

# 36. Use a lambda function to find the maximum of two numbers.
max_two = lambda a, b: a if a > b else b

# 37. Lambda function to calculate simple interest.
simple_int = lambda p, r, t: (p * r * t) / 100

# 38. Use map() and lambda to generate a list containing squares.
squares_list = list(map(lambda x: x**2, [1, 2, 3, 4, 5]))

# 39. Use map() with lambda to calculate the cube of every element in a list.
cubes_list = list(map(lambda x: x**3, [1, 2, 3, 4, 5]))

# 40. Use map() and lambda to create a third list containing the sum of corresponding elements.
sum_lists = list(map(lambda x, y: x + y, [1, 2], [3, 4]))

# 41. Use filter() and lambda to extract all even numbers.
evens = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]))

# 42. Use filter() and lambda to identify prime numbers.
primes = list(filter(lambda x: is_prime(x), range(2, 20)))

# 43. Use filter() and lambda to extract positive numbers.
positives = list(filter(lambda x: x > 0, [-1, 2, -3, 4]))

# 44. Use filter() and lambda to find numbers greater than 50.
greater_50 = list(filter(lambda x: x > 50, [10, 60, 30, 80]))

# 45. Use filter() and lambda to find words having more than five characters.
long_words = list(filter(lambda w: len(w) > 5, ["apple", "cat", "banana", "dog"]))

# 46. Sort a list of words according to their length using lambda.
sorted_words = sorted(["apple", "cat", "banana", "dog"], key=lambda w: len(w))

# 47. Sort a list of tuples (name, marks) according to marks using lambda.
sorted_students = sorted([("Alice", 85), ("Bob", 92), ("Charlie", 78)], key=lambda s: s[1])

# 48. Sort employee records (name, salary) according to salary using lambda.
sorted_employees = sorted([{"name": "A", "salary": 60000}, {"name": "B", "salary": 45000}], key=lambda e: e["salary"])



# 49. Process student names and marks: avg, filter > 75, sort by marks.
students_data = [("John", 80), ("Emma", 70), ("Harry", 95)]
avg_marks = sum(map(lambda x: x[1], students_data)) / len(students_data)
top_students = list(filter(lambda x: x[1] > 75, students_data))
ranked_students = sorted(students_data, key=lambda x: x[1], reverse=True)

