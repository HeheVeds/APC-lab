import pandas as pd

# Read the CSV file
df = pd.read_csv("students.csv")

# Subjects
subjects = ["Maths", "Science", "English", "Computer"]

# Calculate Total marks
df["Total"] = df[subjects].sum(axis=1)

# Calculate Percentage
df["Percentage"] = df["Total"] / 4

# Calculate Grade
def grade(p):
    if p >= 90:
        return "A+"
    elif p >= 80:
        return "A"
    elif p >= 70:
        return "B"
    elif p >= 60:
        return "C"
    elif p >= 50:
        return "D"
    else:
        return "F"

df["Grade"] = df["Percentage"].apply(grade)

# Class average
average = df["Percentage"].mean()

# Find topper
topper = df.loc[df["Percentage"].idxmax()]

# Students who failed
failed = df[df["Percentage"] < 40]

# Display results
print("STUDENT PERFORMANCE")
print(df)

print("\nClass Average:", round(average, 2), "%")

print("\nTopper:")
print("Name:", topper["Name"])
print("Percentage:", topper["Percentage"], "%")
print("Grade:", topper["Grade"])

print("\nStudents Below 40%:")

if len(failed) == 0:
    print("No students failed.")
else:
    print(failed[["Name", "Percentage", "Grade"]])

# Save the result
df.to_csv("student_performance.csv", index=False)
