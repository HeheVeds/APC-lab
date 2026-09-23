import math

# 1. Employee and Manager

class Employee1:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Salary:", self.salary)


class Manager1(Employee1):
    def __init__(self, emp_id, name, salary, department):
        super().__init__(emp_id, name, salary)
        self.department = department

    def display_manager(self):
        self.display()
        print("Department:", self.department)
        print("Annual Salary:", self.salary * 12)


m1 = Manager1(101, "Rahul", 50000, "IT")
m1.display_manager()


# 2. Vehicle and Car

class Vehicle2:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)


class Car2(Vehicle2):
    def __init__(self, brand, model, fuel_type, price):
        super().__init__(brand, model)
        self.fuel_type = fuel_type
        self.price = price

    def display_car(self):
        self.display()
        print("Fuel Type:", self.fuel_type)
        print("Price:", self.price)

    def discounted_price(self):
        return self.price - (self.price * 0.10)


c2 = Car2("Toyota", "Glanza", "Petrol", 800000)
c2.display_car()
print("Discounted Price:", c2.discounted_price())


# 3. Academic and Sports

class Academic3:
    def __init__(self, marks):
        self.marks = marks


class Sports3:
    def __init__(self, points):
        self.points = points


class Student3(Academic3, Sports3):
    def __init__(self, marks, points):
        Academic3.__init__(self, marks)
        Sports3.__init__(self, points)

    def performance(self):
        overall = self.marks + self.points
        print("Academic Marks:", self.marks)
        print("Sports Points:", self.points)
        print("Overall Performance:", overall)


s3 = Student3(85, 10)
s3.performance()


# 4. Personal and Professional Details

class PersonalDetails4:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class ProfessionalDetails4:
    def __init__(self, emp_id, designation, salary):
        self.emp_id = emp_id
        self.designation = designation
        self.salary = salary


class Employee4(PersonalDetails4, ProfessionalDetails4):
    def __init__(self, name, age, emp_id, designation, salary):
        PersonalDetails4.__init__(self, name, age)
        ProfessionalDetails4.__init__(
            self, emp_id, designation, salary
        )

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.emp_id)
        print("Designation:", self.designation)
        print("Salary:", self.salary)


e4 = Employee4("Priya", 25, 101, "Developer", 50000)
e4.display()


# 5. Person, Student and ResearchStudent

class Person5:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student5(Person5):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course


class ResearchStudent5(Student5):
    def __init__(self, name, age, roll_no, course, topic, guide):
        super().__init__(name, age, roll_no, course)
        self.topic = topic
        self.guide = guide

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll No:", self.roll_no)
        print("Course:", self.course)
        print("Research Topic:", self.topic)
        print("Guide Name:", self.guide)


r5 = ResearchStudent5(
    "Sneha",
    23,
    15,
    "Computer Science",
    "Artificial Intelligence",
    "Dr. Sharma"
)
r5.display()


# 6. BankAccount, SavingsAccount and PremiumSavingsAccount

class BankAccount6:
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = balance


class SavingsAccount6(BankAccount6):
    def __init__(self, account_no, balance, interest_rate):
        super().__init__(account_no, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate / 100


class PremiumSavingsAccount6(SavingsAccount6):
    def __init__(self, account_no, balance, interest_rate, benefits):
        super().__init__(account_no, balance, interest_rate)
        self.benefits = benefits

    def display(self):
        print("Account Number:", self.account_no)
        print("Balance:", self.balance)
        print("Interest Rate:", self.interest_rate, "%")
        print("Interest:", self.calculate_interest())
        print("Benefits:", self.benefits)


p6 = PremiumSavingsAccount6(
    12345,
    100000,
    6,
    "Free ATM and Insurance"
)
p6.display()


# 7. Shape, Circle, Rectangle and Triangle

class Shape7:
    def display(self):
        print("This is a shape")


class Circle7(Shape7):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius


class Rectangle7(Shape7):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


class Triangle7(Shape7):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


circle7 = Circle7(5)
rectangle7 = Rectangle7(10, 5)
triangle7 = Triangle7(8, 6)

print("Circle Area:", circle7.area())
print("Rectangle Area:", rectangle7.area())
print("Triangle Area:", triangle7.area())


# 8. Employee, Manager, Developer and Tester

class Employee8:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary


class Manager8(Employee8):
    def salary(self):
        return self.basic_salary + self.basic_salary * 0.30


class Developer8(Employee8):
    def salary(self):
        return self.basic_salary + self.basic_salary * 0.20


class Tester8(Employee8):
    def salary(self):
        return self.basic_salary + self.basic_salary * 0.15


manager8 = Manager8(101, "Amit", 50000)
developer8 = Developer8(102, "Riya", 50000)
tester8 = Tester8(103, "Neha", 50000)

print("Manager Salary:", manager8.salary())
print("Developer Salary:", developer8.salary())
print("Tester Salary:", tester8.salary())


# 9. Person, Student, Faculty and TeachingAssistant

class Person9:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student9(Person9):
    def __init__(self, name, age, roll_no):
        Person9.__init__(self, name, age)
        self.roll_no = roll_no


class Faculty9(Person9):
    def __init__(self, name, age, faculty_id):
        Person9.__init__(self, name, age)
        self.faculty_id = faculty_id


class TeachingAssistant9(Student9, Faculty9):
    def __init__(self, name, age, roll_no, faculty_id):
        Person9.__init__(self, name, age)
        self.roll_no = roll_no
        self.faculty_id = faculty_id

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll No:", self.roll_no)
        print("Faculty ID:", self.faculty_id)


ta9 = TeachingAssistant9("Kiran", 22, 25, "F101")
ta9.display()


# 10. Vehicle, Car, Bike, SportsCar and ElectricBike

class Vehicle10:
    def __init__(self, brand):
        self.brand = brand


class Car10(Vehicle10):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model


class Bike10(Vehicle10):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model


class SportsCar10(Car10):
    def __init__(self, brand, model, speed):
        super().__init__(brand, model)
        self.speed = speed

    def display(self):
        print("Sports Car:", self.brand)
        print("Model:", self.model)
        print("Speed:", self.speed, "km/h")


class ElectricBike10(Bike10):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.battery = battery

    def display(self):
        print("Electric Bike:", self.brand)
        print("Model:", self.model)
        print("Battery:", self.battery, "kWh")


sports_car10 = SportsCar10("BMW", "M4", 250)
electric_bike10 = ElectricBike10("Ather", "450X", 3.7)

sports_car10.display()
electric_bike10.display()


# 11. Student and Result

class Student11:
    def __init__(self, roll_no, name, course):
        self.roll_no = roll_no
        self.name = name
        self.course = course


class Result11(Student11):
    def __init__(self, roll_no, name, course, m1, m2, m3):
        super().__init__(roll_no, name, course)
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def calculate_result(self):
        total = self.m1 + self.m2 + self.m3
        percentage = total / 3

        if percentage >= 75:
            grade = "A"
        elif percentage >= 60:
            grade = "B"
        elif percentage >= 50:
            grade = "C"
        else:
            grade = "D"

        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Course:", self.course)
        print("Total Marks:", total)
        print("Percentage:", percentage)
        print("Grade:", grade)


result11 = Result11(
    10,
    "Vedika",
    "CSE",
    85,
    78,
    90
)
result11.calculate_result()


# 12. Product and ElectronicProduct

class Product12:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price


class ElectronicProduct12(Product12):
    def __init__(self, product_id, name, price, brand, warranty):
        super().__init__(product_id, name, price)
        self.brand = brand
        self.warranty = warranty

    def display(self):
        discount = self.price * 0.10
        final_price = self.price - discount

        print("Product ID:", self.product_id)
        print("Name:", self.name)
        print("Brand:", self.brand)
        print("Price:", self.price)
        print("Warranty:", self.warranty, "years")
        print("Final Price:", final_price)


product12 = ElectronicProduct12(
    101,
    "Laptop",
    60000,
    "HP",
    2
)
product12.display()


#polymorphism:



# 1. Shape - Runtime Polymorphism


class Shape:
    def area(self):
        print("Area of shape")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


shapes = [Circle(5), Rectangle(10, 5), Triangle(8, 6)]

for shape in shapes:
    print("Area:", shape.area())



# 2. Employee - Runtime Polymorphism


class Employee:
    def calculate_salary(self):
        return 0


class Manager(Employee):
    def calculate_salary(self):
        return 50000 + 15000


class Developer(Employee):
    def calculate_salary(self):
        return 50000 + 10000


class Tester(Employee):
    def calculate_salary(self):
        return 50000 + 7500


employees = [Manager(), Developer(), Tester()]

for employee in employees:
    print("Salary:", employee.calculate_salary())



# 3. Vehicle - Runtime Polymorphism


class Vehicle:
    def start(self):
        print("Vehicle is starting")


class Car(Vehicle):
    def start(self):
        print("Car starts with a key")


class Bike(Vehicle):
    def start(self):
        print("Bike starts with a self-start button")


class Bus(Vehicle):
    def start(self):
        print("Bus starts with an engine")


vehicles = [Car(), Bike(), Bus()]

for vehicle in vehicles:
    vehicle.start()


# 4. Animal - Runtime Polymorphism


class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dog says: Woof")


class Cat(Animal):
    def sound(self):
        print("Cat says: Meow")


class Cow(Animal):
    def sound(self):
        print("Cow says: Moo")


class Lion(Animal):
    def sound(self):
        print("Lion says: Roar")


animals = [Dog(), Cat(), Cow(), Lion()]

for animal in animals:
    animal.sound()



# 5. Notification - Runtime Polymorphism


class Notification:
    def send(self):
        print("Sending notification")


class EmailNotification(Notification):
    def send(self):
        print("Sending notification through Email")


class SMSNotification(Notification):
    def send(self):
        print("Sending notification through SMS")


class PushNotification(Notification):
    def send(self):
        print("Sending notification through Push Notification")


notifications = [
    EmailNotification(),
    SMSNotification(),
    PushNotification()
]

for notification in notifications:
    notification.send()



# 6. Student - Runtime Polymorphism


class Student:
    def calculate_grade(self, marks):
        return "Grade not defined"


class EngineeringStudent(Student):
    def calculate_grade(self, marks):
        if marks >= 75:
            return "A"
        elif marks >= 60:
            return "B"
        else:
            return "C"


class MedicalStudent(Student):
    def calculate_grade(self, marks):
        if marks >= 80:
            return "A"
        elif marks >= 65:
            return "B"
        else:
            return "C"


class ManagementStudent(Student):
    def calculate_grade(self, marks):
        if marks >= 70:
            return "A"
        elif marks >= 55:
            return "B"
        else:
            return "C"


students = [
    EngineeringStudent(),
    MedicalStudent(),
    ManagementStudent()
]

marks = [78, 82, 72]

for student, mark in zip(students, marks):
    print("Grade:", student.calculate_grade(mark))



# 7. BankAccount - Runtime Polymorphism


class BankAccount:
    def calculate_interest(self, balance):
        return 0


class SavingsAccount(BankAccount):
    def calculate_interest(self, balance):
        return balance * 0.06


class CurrentAccount(BankAccount):
    def calculate_interest(self, balance):
        return balance * 0.02


class FixedDepositAccount(BankAccount):
    def calculate_interest(self, balance):
        return balance * 0.08


accounts = [
    SavingsAccount(),
    CurrentAccount(),
    FixedDepositAccount()
]

balance = 100000

for account in accounts:
    print("Interest:", account.calculate_interest(balance))



# 8. Report - Runtime Polymorphism


class Report:
    def generate(self):
        print("Generating report")


class PDFReport(Report):
    def generate(self):
        print("Generating PDF report")


class ExcelReport(Report):
    def generate(self):
        print("Generating Excel report")


class HTMLReport(Report):
    def generate(self):
        print("Generating HTML report")


def generate_report(report):
    report.generate()


generate_report(PDFReport())
generate_report(ExcelReport())
generate_report(HTMLReport())



# 9. Distance - Operator Overloading (+)


class Distance:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __add__(self, other):
        total_inches = self.inches + other.inches
        feet = self.feet + other.feet

        feet += total_inches // 12
        inches = total_inches % 12

        return Distance(feet, inches)

    def display(self):
        print("Distance:", self.feet, "feet", self.inches, "inches")


d1 = Distance(5, 8)
d2 = Distance(4, 7)

d3 = d1 + d2
d3.display()



# 10. Student - Operator Overloading (> and <)


class StudentMarks:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __gt__(self, other):
        return self.marks > other.marks

    def __lt__(self, other):
        return self.marks < other.marks


student1 = StudentMarks("Rahul", 85)
student2 = StudentMarks("Amit", 75)

print("Student 1 has greater marks:", student1 > student2)
print("Student 1 has smaller marks:", student1 < student2)



# 11. Product - Operator Overloading (== and >)


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.price == other.price

    def __gt__(self, other):
        return self.price > other.price


product1 = Product("Laptop", 60000)
product2 = Product("Mobile", 60000)

print("Both products have same price:", product1 == product2)
print("Product 1 is more expensive:", product1 > product2)


#abstraction:

from abc import ABC, abstractmethod
import math



# 1. Abstract Shape


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


c = Circle(5)
r = Rectangle(10, 5)
t = Triangle(8, 6)

print("Circle Area:", c.area())
print("Rectangle Area:", r.area())
print("Triangle Area:", t.area())


#
# 2. Abstract Vehicle


class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Car starts with a key")

    def stop(self):
        print("Car stops using brakes")


class Bike(Vehicle):
    def start(self):
        print("Bike starts with self-start")

    def stop(self):
        print("Bike stops using brakes")


class Bus(Vehicle):
    def start(self):
        print("Bus starts with engine")

    def stop(self):
        print("Bus stops at the bus stop")


car = Car()
bike = Bike()
bus = Bus()

car.start()
car.stop()

bike.start()
bike.stop()

bus.start()
bus.stop()



# 3. Abstract BankAccount

class BankAccount(ABC):

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass


class SavingsAccount(BankAccount):
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Savings Account Balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Savings Account Balance:", self.balance)
        else:
            print("Insufficient Balance")


class CurrentAccount(BankAccount):
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Current Account Balance:", self.balance)

    def withdraw(self, amount):
        self.balance -= amount
        print("Current Account Balance:", self.balance)


s = SavingsAccount(10000)
s.deposit(2000)
s.withdraw(3000)

ca = CurrentAccount(20000)
ca.deposit(5000)
ca.withdraw(4000)



# 4. Abstract FoodOrder


class FoodOrder(ABC):

    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def delivery_charge(self):
        pass


class RestaurantOrder(FoodOrder):
    def __init__(self, food_price):
        self.food_price = food_price

    def calculate_bill(self):
        return self.food_price

    def delivery_charge(self):
        return 0


class HomeDeliveryOrder(FoodOrder):
    def __init__(self, food_price):
        self.food_price = food_price

    def calculate_bill(self):
        return self.food_price

    def delivery_charge(self):
        return 50


restaurant = RestaurantOrder(500)
print("Restaurant Bill:", restaurant.calculate_bill())
print("Delivery Charge:", restaurant.delivery_charge())
print("Total:", restaurant.calculate_bill() + restaurant.delivery_charge())

home = HomeDeliveryOrder(500)
print("Home Delivery Bill:", home.calculate_bill())
print("Delivery Charge:", home.delivery_charge())
print("Total:", home.calculate_bill() + home.delivery_charge())



# 5. Abstract Patient


class Patient(ABC):

    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def treatment(self):
        pass


class InPatient(Patient):
    def calculate_bill(self):
        return 5000

    def treatment(self):
        return "In-patient treatment with hospital stay"


class OutPatient(Patient):
    def calculate_bill(self):
        return 1000

    def treatment(self):
        return "Out-patient consultation"


class EmergencyPatient(Patient):
    def calculate_bill(self):
        return 8000

    def treatment(self):
        return "Emergency treatment"


patients = [
    InPatient(),
    OutPatient(),
    EmergencyPatient()
]

for patient in patients:
    print("Treatment:", patient.treatment())
    print("Bill:", patient.calculate_bill())



# 6. Abstract Transport


class Transport(ABC):

    @abstractmethod
    def calculate_fare(self, distance):
        pass


class Bus(Transport):
    def calculate_fare(self, distance):
        return distance * 2


class Train(Transport):
    def calculate_fare(self, distance):
        return distance * 1.5


class Taxi(Transport):
    def calculate_fare(self, distance):
        return distance * 10


class Flight(Transport):
    def calculate_fare(self, distance):
        return distance * 15


distance = 100

print("Bus Fare:", Bus().calculate_fare(distance))
print("Train Fare:", Train().calculate_fare(distance))
print("Taxi Fare:", Taxi().calculate_fare(distance))
print("Flight Fare:", Flight().calculate_fare(distance))



# 7. Abstract Question


class Question(ABC):

    @abstractmethod
    def evaluate_answer(self, answer):
        pass


class MCQQuestion(Question):
    def __init__(self, correct_answer):
        self.correct_answer = correct_answer

    def evaluate_answer(self, answer):
        if answer == self.correct_answer:
            return "Correct"
        else:
            return "Incorrect"


class TrueFalseQuestion(Question):
    def __init__(self, correct_answer):
        self.correct_answer = correct_answer

    def evaluate_answer(self, answer):
        if answer == self.correct_answer:
            return "Correct"
        else:
            return "Incorrect"


class DescriptiveQuestion(Question):
    def evaluate_answer(self, answer):
        if len(answer) >= 20:
            return "Answer Accepted"
        else:
            return "Answer Too Short"


mcq = MCQQuestion("B")
print("MCQ:", mcq.evaluate_answer("B"))

tf = TrueFalseQuestion("True")
print("True/False:", tf.evaluate_answer("True"))

descriptive = DescriptiveQuestion()
print(
    "Descriptive:",
    descriptive.evaluate_answer(
        "Python is an object oriented programming language."
    )
)



# 8. Abstract Authentication


class Authentication(ABC):

    @abstractmethod
    def authenticate(self):
        pass


class PasswordAuthentication(Authentication):
    def authenticate(self):
        print("Authenticated using Password")


class OTPAuthentication(Authentication):
    def authenticate(self):
        print("Authenticated using OTP")


class BiometricAuthentication(Authentication):
    def authenticate(self):
        print("Authenticated using Biometric")


password = PasswordAuthentication()
otp = OTPAuthentication()
biometric = BiometricAuthentication()

password.authenticate()
otp.authenticate()
biometric.authenticate()