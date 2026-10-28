
import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("User Education Page")
root.geometry("400x450")

# Heading
tk.Label(root, text="User Education Details",
         font=("Arial", 18, "bold")).pack(pady=15)

# Name
tk.Label(root, text="Name").pack()
name = tk.Entry(root)
name.pack()

# Email
tk.Label(root, text="Email").pack()
email = tk.Entry(root)
email.pack()

# Password
tk.Label(root, text="Password").pack()
password = tk.Entry(root, show="*")
password.pack()

# Gender
tk.Label(root, text="Gender").pack()
gender = tk.StringVar()
tk.Radiobutton(root, text="Male", variable=gender,
               value="Male").pack()
tk.Radiobutton(root, text="Female", variable=gender,
               value="Female").pack()

# Course
tk.Label(root, text="Select Course").pack()
course = tk.StringVar()
course.set("Python")

tk.OptionMenu(root, course, "Python", "Java",
              "C++", "Web Development").pack()

# Submit Function
def submit():
    if name.get() == "" or email.get() == "":
        messagebox.showwarning("Warning", "Please fill all details")
    else:
        messagebox.showinfo("Success", "Registration Successful!")

# Submit Button
tk.Button(root, text="Submit", command=submit,
          bg="green", fg="white").pack(pady=20)

# Run Application
root.mainloop()
```
