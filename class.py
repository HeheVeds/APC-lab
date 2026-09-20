


# 1. Student Class
class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def display(self):
        percentage = sum(self.marks) / len(self.marks)
        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Percentage:", percentage, "%")
        print()


print("----- 1. STUDENT -----")
s1 = Student(1, "Vedika", [85, 90, 88, 92, 86])
s2 = Student(2, "Riya", [80, 75, 85, 90, 82])

s1.display()
s2.display()


# 2. Employee Class
class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary

    def calculate_salary(self):
        hra = self.basic_salary * 0.20
        da = self.basic_salary * 0.10
        gross = self.basic_salary + hra + da

        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Basic Salary:", self.basic_salary)
        print("HRA:", hra)
        print("DA:", da)
        print("Gross Salary:", gross)
        print()


print("----- 2. EMPLOYEE -----")
e1 = Employee(101, "Rahul", 30000)
e1.calculate_salary()


# 3. Rectangle Class
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


print("----- 3. RECTANGLE -----")
r1 = Rectangle(10, 5)
print("Length:", r1.length)
print("Breadth:", r1.breadth)
print("Area:", r1.area())
print("Perimeter:", r1.perimeter())
print()


# 4. Circle Class
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def circumference(self):
        return 2 * 3.14 * self.radius


print("----- 4. CIRCLE -----")
c1 = Circle(7)
print("Radius:", c1.radius)
print("Area:", c1.area())
print("Circumference:", c1.circumference())
print()


# 5. Book Class
class Book:
    def __init__(self, book_id, title, author, price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
        print()


print("----- 5. BOOK -----")
b1 = Book(101, "Python Basics", "John", 400)
b2 = Book(102, "Java Programming", "James", 500)
b3 = Book(103, "Data Structures", "Mark", 600)

b1.display()
b2.display()
b3.display()


# 6. Electricity Bill Class
class ElectricityBill:
    def __init__(self, consumer_no, consumer_name, units):
        self.consumer_no = consumer_no
        self.consumer_name = consumer_name
        self.units = units

    def calculate_bill(self):
        if self.units <= 100:
            bill = self.units * 2
        elif self.units <= 200:
            bill = (100 * 2) + (self.units - 100) * 3
        else:
            bill = (100 * 2) + (100 * 3) + (self.units - 200) * 5

        return bill

    def display(self):
        print("Consumer Number:", self.consumer_no)
        print("Consumer Name:", self.consumer_name)
        print("Units Consumed:", self.units)
        print("Electricity Bill:", self.calculate_bill())
        print()


print("----- 6. ELECTRICITY BILL -----")
eb1 = ElectricityBill(1001, "Amit", 250)
eb1.display()


# 7. Mobile Phone Class
class MobilePhone:
    def __init__(self, brand, model, storage, price):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Storage:", self.storage)
        print("Price:", self.price)

    def discounted_price(self, discount):
        return self.price - (self.price * discount / 100)


print("----- 7. MOBILE PHONE -----")
m1 = MobilePhone("Samsung", "S24", "256 GB", 60000)
m1.display()
print("Price after 10% discount:", m1.discounted_price(10))
print()


# 8. Patient Class
class Patient:
    def __init__(self, patient_id, name, age, disease, consultation_fee):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease
        self.consultation_fee = consultation_fee

    def display(self):
        print("Patient ID:", self.patient_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Disease:", self.disease)
        print("Consultation Fee:", self.consultation_fee)

    def total_bill(self, medicine_fee):
        return self.consultation_fee + medicine_fee


print("----- 8. PATIENT -----")
p1 = Patient(501, "Sneha", 25, "Fever", 500)
p1.display()
print("Total Bill:", p1.total_bill(300))
print()


# 9. ATM Class
class ATM:
    def __init__(self, account_no, name, balance):
        self.account_no = account_no
        self.name = name
        self.balance = balance

    def check_balance(self):
        print("Current Balance:", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print("Amount Deposited:", amount)
        print("New Balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount Withdrawn:", amount)
            print("Remaining Balance:", self.balance)
        else:
            print("Insufficient Balance")

    def account_details(self):
        print("Account Number:", self.account_no)
        print("Account Holder:", self.name)
        print("Balance:", self.balance)


print("----- 9. ATM -----")

atm = ATM(12345, "Vedika", 10000)

while True:
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Account Details")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        atm.check_balance()

    elif choice == 2:
        amount = float(input("Enter amount to deposit: "))
        atm.deposit(amount)

    elif choice == 3:
        amount = float(input("Enter amount to withdraw: "))
        atm.withdraw(amount)

    elif choice == 4:
        atm.account_details()

    elif choice == 5:
        print("Thank you for using ATM.")
        break

    else:
        print("Invalid choice")


# 10. Vehicle Class
class Vehicle:
    def __init__(self, vehicle_no, model, rental_rate, availability):
        self.vehicle_no = vehicle_no
        self.model = model
        self.rental_rate = rental_rate
        self.availability = availability

    def rent_vehicle(self):
        if self.availability:
            self.availability = False
            print("Vehicle rented successfully.")
        else:
            print("Vehicle is not available.")

    def return_vehicle(self, days):
        if not self.availability:
            self.availability = True
            charge = self.rental_rate * days
            print("Vehicle returned successfully.")
            print("Rental Charges:", charge)
        else:
            print("Vehicle was not rented.")


print("\n----- 10. VEHICLE -----")

v1 = Vehicle("MH09AB1234", "Swift", 1000, True)

print("Vehicle Number:", v1.vehicle_no)
print("Model:", v1.model)
print("Rental Rate per Day:", v1.rental_rate)

v1.rent_vehicle()

days = int(input("Enter number of rental days: "))
v1.return_vehicle(days)