

A = []
B = []

print("Enter elements of Matrix A:")
for i in range(3):
    row = []
    for j in range(3):
        row.append(int(input(f"A[{i}][{j}]: ")))
    A.append(row)

print("\nEnter elements of Matrix B:")
for i in range(3):
    row = []
    for j in range(3):
        row.append(int(input(f"B[{i}][{j}]: ")))
    B.append(row)

# Addition
add = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(A[i][j] + B[i][j])
    add.append(row)

# Subtraction
sub = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(A[i][j] - B[i][j])
    sub.append(row)

# Display results
print("\nMatrix Addition (A + B):")
for row in add:
    print(row)

print("\nMatrix Subtraction (A - B):")
for row in sub:
    print(row)
