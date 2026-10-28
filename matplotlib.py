
import matplotlib.pyplot as plt

# Sample Data
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

# 1. Line Graph
plt.plot(x, y, marker='o')
plt.title("Line Graph")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()

# 2. Bar Graph
plt.bar(x, y)
plt.title("Bar Graph")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()

# 3. Pie Chart
subjects = ['Python', 'Java', 'C++', 'HTML']
marks = [30, 25, 20, 25]
plt.pie(marks, labels=subjects, autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()

# 4. Histogram
data = [10, 20, 20, 30, 30, 30, 40, 40, 50, 50, 60]
plt.hist(data, bins=5, edgecolor='black')
plt.title("Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()

# 5. Scatter Plot
plt.scatter(x, y)
plt.title("Scatter Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()

# 6. Horizontal Bar Graph
plt.barh(x, y)
plt.title("Horizontal Bar Graph")
plt.xlabel("Values")
plt.ylabel("Categories")
plt.show()

# 7. Area Plot
plt.fill_between(x, y, alpha=0.5)
plt.title("Area Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()

# 8. Box Plot
data = [10, 20, 25, 30, 35, 40, 45, 50, 60]
plt.boxplot(data)
plt.title("Box Plot")
plt.ylabel("Values")
plt.show()

print("All 8 graphs displayed successfully!")
```

