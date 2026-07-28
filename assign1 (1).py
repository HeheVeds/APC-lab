# 1)program that reads a value of n and check if the nmber is zero or non zero

n = int(input("Enter a number"))
if(n==0):
    print("Number is zero")
else:
    print("N is a non-zero number")


# 2)find the largest number from 2 numbers and accept user input 

a = int(input("enter 1st number"))
b =  int(input("enter 2nd number"))
if(a>b):
    print("a is the greater number")
else:
    print("b is greater number")



# 3)take input from user and check whether number is positive or negative

n = int(input("Enter a number"))
if(n<0):
    print("number is negative")
else:
    print("number is positive")


# 4)take input character from user and check whether it is vowel or consonant

char = input("enter a character")
if char =='a' or char =='e' or char=='i' or char == 'o' or char == 'u':
    print("entered character is a vowel")
else:
    print("not a vowel")


# 5)program to evaluate student performance(percent <=90:excellent,per>=80:very good,per>=70:good,per>=60:average else poor)
per = float(input("enter the percentage obtained"))
if(per>=90):
    print("excellent")
elif(per>=80):
    print("very good")
elif(per>=70):
    print("good")
elif(per>=60):
    print("average")
else:
    print("poor performance")


# 6)find largest and smallest from 3 numbers except user input
a = int(input("enter 1st number"))
b = int(input("enter 2nd number"))
c = int(input("enter 3rd number"))

if (a >= b) and (a >= c):
    largest = a
elif (b >= a) and (b >= c):
    largest = b
else:
    largest = c

print("largest is:",largest)


# 7)check if given number is even or odd

n = int(input("enter a number"))
if(n%2==0):
    print("number is even")
else:
    print("number is odd")

# 8)check if year is leap year or not

year = int(input("enter year"))
if(year % 4 == 0 and year % 100 !=0) or (year % 400 == 0):
    print("year is leap year")
else:
    print("year is not leap year")