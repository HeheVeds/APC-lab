#1.Write a program to input a string and display its length without using the len() function. 

string = input("Enter a string: ")

count = 0
for i in string:
    count += 1

print("Length of string:", count)


#2.Count the number of vowels, consonants, digits, spaces, and special characters in a given string.
string = input("Enter a string: ")

vowels = consonants = digits = spaces = special = 0

for ch in string:
    if ch.lower() in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1
    else:
        special += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special Characters:", special) 


#3.Reverse the given string without using built-in reverse functions
string = input("Enter a string: ")

reverse = " "

for ch in string:
    reverse = ch + reverse

print("Reversed string:", reverse)


#4.Check whether the entered string is a palindrome. 
string = input("Enter a string: ")

reverse = " "

for ch in string:
    reverse = ch + reverse

if string == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")
   

#5.Count the number of uppercase and lowercase letters in a string. 
string = input("Enter a string: ")

upper = lower = 0

for ch in string:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1

print("Uppercase letters:", upper)
print("Lowercase letters:", lower)


#6.Replace all occurrences of a given character with another character. 
string = input("Enter a string: ")
old = input("Enter character to replace: ")
new = input("Enter new character: ")

result = " "

for ch in string:
    if ch == old:
        result += new
    else:
        result += ch

print("New string:", result)


#7.Remove all spaces from the input string
string = input("Enter a string: ")

result = " "

for ch in string:
    if ch != " ":
        result += ch

print("String without spaces:", result)


#8.Find the number of times a specified character appears in a string. 
string = input("Enter a string: ")
char = input("Enter character to count: ")

count = 0

for ch in string:
    if ch == char:
        count += 1

print("Frequency:", count)


#9.Print the first and last character of a string
string = input("Enter a string: ")

if string == "":
    print("Empty string")
else:
    print("First character:", string[0])
    print("Last character:", string[-1])


#11.Count the total number of words in a sentence. 
sentence = input("Enter a sentence: ")

words = sentence.split()

print("Total words:", len(words))


#12.Find the longest word in a given sentence.
sentence = input("Enter a sentence: ")

words = sentence.split()
longest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)

#13.Find the shortest word in a sentence.
sentence = input("Enter a sentence: ")

words = sentence.split()
shortest = words[0]

for word in words:
    if len(word) < len(shortest):
        shortest = word

print("Shortest word:", shortest)


#14.Convert the first letter of every word to uppercase. 
sentence = input("Enter a sentence: ")

print("Title Case:", sentence.title())

#15.Print all duplicate characters in a string. 
string = input("Enter a string: ")

printed = ""

for ch in string:
    if string.count(ch) > 1 and ch not in printed:
        print(ch)
        printed += ch


#16.Display the frequency of every character in a string
string = input("Enter a string: ")

checked = ""

for ch in string:
    if ch not in checked:
        print(ch, ":", string.count(ch))
        checked += ch


#17.Remove duplicate characters while maintaining the original order.

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

a = sorted(str1.replace(" ", "").lower())
b = sorted(str2.replace(" ", "").lower())

if a == b:
    print("Strings are Anagrams")
else:
    print("Strings are Not Anagrams")

#18.Remove duplicate characters while maintaining the original order. 
string = input("Enter a string: ")

result = ""

for ch in string:
    if ch not in result:
        result += ch

print("After removing duplicates:", result)

#19.Check whether a given substring exists in the main string. 
string = input("Enter main string: ")
sub = input("Enter substring: ")

if sub in string:
    print("Substring Found")
else:
    print("Substring Not Found")


#20.Count how many times a specific word appears in a sentence
sentence = input("Enter a sentence: ")
word = input("Enter word to search: ")

words = sentence.split()

count = 0

for w in words:
    if w == word:
        count += 1

print("Occurrences:", count)


#21.Validate a password based on these conditions: Minimum 8 characters At least one uppercase letter One lowercase letter 	One digit	One special character
password = input("Enter password: ")

upper = lower = digit = special = False

for ch in password:
    if ch.isupper():
        upper = True
    elif ch.islower():
        lower = True
    elif ch.isdigit():
        digit = True
    else:
        special = True

if len(password) >= 8 and upper and lower and digit and special:
    print("Valid Password")
else:
    print("Invalid Password")

#23.Compress repeated characters and return the original string if compression does not reduce the length. 
string = input("Enter a string: ")

compressed = ""
count = 1

for i in range(len(string)):
    if i < len(string)-1 and string[i] == string[i+1]:
        count += 1
    else:
        compressed += string[i] + str(count)
        count = 1

if len(compressed) < len(string):
    print("Compressed:", compressed)
else:
    print("Original:", string)


#24.Find the character with the highest frequency. 
string = input("Enter a string: ")

max_char = ""
max_count = 0

for ch in string:
    if string.count(ch) > max_count:
        max_count = string.count(ch)
        max_char = ch

print("Most Frequent Character:", max_char)
print("Frequency:", max_count)


#27.Validate whether a given email address follows a valid format. 
email = input("Enter email: ")

if "@" in email and "." in email and email.index("@") < email.rindex("."):
    print("Valid Email")
else:
    print("Invalid Email")


#28.Count the frequency of every word in a paragraph.
paragraph = input("Enter a paragraph: ")

words = paragraph.lower().split()

freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

for word in freq:
    print(word, ":", freq[word])


#29.Reverse the order of words in a sentence without changing the words themselves. Example:
# Input: Python is easy  Output: easy is Python
sentence = input("Enter a sentence: ")

words = sentence.split()

for i in range(len(words)-1, -1, -1):
    print(words[i], end=" ")


#30.Check whether one string is a rotation of another. Example:ABCD CDBA   Output: Yes
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if len(str1) == len(str2) and str2 in (str1 + str1):
    print("Yes, it is a rotation.")
else:
    print("No, it is not a rotation.")
