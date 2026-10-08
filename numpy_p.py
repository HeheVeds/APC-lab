import numpy as np


# 1. One-dimensional array and its properties


arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

print("\n1. One-Dimensional Array")
print("Array:", arr)
print("Size:", arr.size)
print("Data type:", arr.dtype)
print("Number of dimensions:", arr.ndim)



# 2. Arithmetic operations on two arrays


a = np.array([10, 20, 30, 40, 50])
b = np.array([2, 4, 5, 8, 10])

print("\n2. Arithmetic Operations")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)



# 3. Maximum, minimum, sum and average


arr = np.array([10, 25, 15, 40, 30, 5, 50, 35, 20, 45])

print("\n3. Array Statistics")
print("Array:", arr)
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
print("Sum:", np.sum(arr))
print("Average:", np.mean(arr))


# 4. Even and odd numbers using Boolean indexing


arr = np.arange(1, 21)

even = arr[arr % 2 == 0]
odd = arr[arr % 2 != 0]

print("\n4. Even and Odd Numbers")
print("Even numbers:", even)
print("Odd numbers:", odd)


# 5. Reshaping an array


arr = np.arange(1, 13)

print("\n5. Reshaping")
print("2 x 6 Matrix:")
print(arr.reshape(2, 6))

print("3 x 4 Matrix:")
print(arr.reshape(3, 4))

print("4 x 3 Matrix:")
print(arr.reshape(4, 3))



# 6. Matrix addition


a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

b = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])

print("\n6. Matrix Addition")
print(a + b)


# 7. Matrix multiplication


a = np.array([[1, 2],
              [3, 4]])

b = np.array([[5, 6],
              [7, 8]])

print("\n7. Matrix Multiplication")
print(np.matmul(a, b))



# 8. Transpose of a matrix


arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])

print("\n8. Transpose")
print("Original Matrix:")
print(arr)

print("Transpose:")
print(arr.T)



# 9. Accessing elements of a 4 x 4 matrix

arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]])

print("\n9. Accessing Matrix Elements")
print("First row:", arr[0])
print("Last column:", arr[:, -1])
print("Diagonal elements:", np.diag(arr))
print("Second and third rows:")
print(arr[1:3])



# 10. Sum of each row and column


arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]])

print("\n10. Row and Column Sum")
print("Sum of each row:", np.sum(arr, axis=1))
print("Sum of each column:", np.sum(arr, axis=0))



# 11. Array slicing


arr = np.arange(1, 21)

print("\n11. Array Slicing")
print("First 5 elements:", arr[:5])
print("Last 5 elements:", arr[-5:])
print("Alternate elements:", arr[::2])
print("Elements in reverse order:", arr[::-1])



# 12. Replace elements greater than 50 with 0


arr = np.array([10, 60, 25, 75, 40, 90, 35, 55, 20, 80])

arr[arr > 50] = 0

print("\n12. Boolean Indexing")
print("Updated array:", arr)


# 13. Ascending and descending order


arr = np.array([45, 12, 78, 23, 9, 56, 34])

print("\n13. Sorting")
print("Original array:", arr)
print("Ascending order:", np.sort(arr))
print("Descending order:", np.sort(arr)[::-1])



# 14. Unique elements


arr = np.array([10, 20, 10, 30, 20, 40, 30, 50, 10])

print("\n14. Unique Elements")
print("Original array:", arr)
print("Unique elements:", np.unique(arr))


# 15. Horizontal and vertical concatenation


a = np.array([[1, 2],
              [3, 4]])

b = np.array([[5, 6],
              [7, 8]])

print("\n15. Concatenation")

print("Horizontal Concatenation:")
print(np.hstack((a, b)))

print("Vertical Concatenation:")
print(np.vstack((a, b)))


# 16. Statistical calculations of marks


marks = np.array([75, 82, 68, 90, 56, 78, 85, 72, 88, 65])

print("\n16. Student Marks Statistics")
print("Marks:", marks)
print("Highest marks:", np.max(marks))
print("Lowest marks:", np.min(marks))
print("Average marks:", np.mean(marks))
print("Median:", np.median(marks))
print("Standard deviation:", np.std(marks))



# 17. Students scoring above class average


marks = np.array([65, 78, 55, 89, 92, 70, 61, 85, 76, 95,
                  68, 72, 80, 58, 90, 74, 63, 87, 69, 82])

average = np.mean(marks)
above_average = marks[marks > average]

print("\n17. Above Average Marks")
print("Class Average:", average)
print("Marks above average:", above_average)


# 18. Create and display a 3D array


arr = np.arange(1, 25).reshape(2, 3, 4)

print("\n18. 3D Array")
print("3D Array:")
print(arr)

print("Number of dimensions:", arr.ndim)
print("Shape:", arr.shape)
print("Size:", arr.size)



# 19. Access elements from a 3D array


arr = np.arange(1, 25).reshape(2, 3, 4)

print("\n19. Accessing 3D Array Elements")
print("3D Array:")
print(arr)

print("First element:", arr[0, 0, 0])
print("Last element:", arr[-1, -1, -1])
print("Element at [0,1,2]:", arr[0, 1, 2])
print("Element at [1,2,3]:", arr[1, 2, 3])