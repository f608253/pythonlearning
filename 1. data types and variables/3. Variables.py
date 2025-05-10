# 1. Create a variable named 'age' and assign it to your age as an integer.
age = 27

# 2. Create a variable called 'height" and assign it to your height in meters as a float.
height = 1.85

# 3. Create a variable called 'name' and assign it to your name as a string.
name = 'Manav'

# 4. Create a variable called 'is_student' and assign it a boolean value indicating whether you are a student or not.
is_student = False

# 5. Print out all these variable.
print(f"Original values: Age: {age}, Height: {height}, Name: {name}, Is Student: {is_student}")

# 6. Increase the 'age' variable by 1 and print it out.
age = age + 1

# 7. Multiply the 'height' variable by 100 to convert it to centimeters and print it out.
height = height * 100

# 8. Add "is my name" to the 'name' variable and print it out.
name = name + " is my name"

# 9. Change 'Is_student' to the opposite and print it out.
is_student = True

print(f"Modified values: Age: {age}, Height: {height}, Name: {name}, Is Student: {is_student}")

# OutPut:
# C:\Users\MANVENDRA\PycharmProjects\pythonProject\.venv\Scripts\python.exe "C:\Users\MANVENDRA\PycharmProjects\PythonLearning\1. data types and variables\3. Variables.py"
# Original values: Age: 27, Height: 1.85, Name: Manav, Is Student: False
# Modified values: Age: 28, Height: 185.0, Name: Manav is my name, Is Student: True

#Basic variable naming rules:

#Start with a letter or underscore (a-z, A-Z,  (_))
age = 25
_secret = "Shhh!"
#2fast = "Speedy!" #This is not a correct variable name

#Use letters , numbers or underscore (az , a_)
user_age_2 = 32
best_friend_1 = "Alice"
#my-variable = 10  # Hyphens are not allowed in variable name

#Case sensitive
Age = 25
age = 27
AGE = 30

print(Age)
print(age)
print(AGE)

#No reserved keywords
#from = "NYJ"  # Not a valid variable name
#if = 5        # This too
print("Hello JI")

#Best practices while giving variable name
# 1. Be descriptive
# 2. Use underscore for spaces
# 3. Keep it simple
max_speed = 300   # This is fine
maximum_speed_of_car_on_highway = 300   #Too long name

#Length of a string
#Using len() function to get the length of a string
greeting = "Hello, world!"
print(f"Greeting is: {greeting}")  #Output: Greeting is: Hello, world!
print(len(greeting)) #Output: 13

#Indexing
print(greeting[0])  #Prints first index of greeting string
print(greeting[-1])  #Prints last character

#Slicing
#The syntax is string[start:end:step]
print(greeting[0:3]) #Hel
print(greeting[1:5]) #ello
print(greeting[::-1]) #!dlrow ,olleH
print(greeting[::1])  #Hello, world!

#Concatenation
full_name = name + ' Singh Yadav'
print(full_name)  #Manav is my name Singh Yadav

#Repetetion with *
name = 'Alice'
chant = name*4
print(chant)  #AliceAliceAliceAlice

#Using string methods
print(name.upper())  #ALICE
print(name.lower())  #alice

#search and replace
print(name.replace('l','x'))  #Axice

#Uppercase
print(greeting.upper())
print(greeting.lower())









