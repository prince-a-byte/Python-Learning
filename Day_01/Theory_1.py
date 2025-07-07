# To Print any thing to the console we use print statement in python:-
print("Hello World!")
print("This is my first Program in Python :)")

# This is a single line comment >> Variables in Pythons:- 

"""To create a variable in Python we can simply type the name of the variable and assign its value >> This is a multiline Comment"""

name = "Narendra Raj" #This is a string data type
age = 18 # This is a integer data type
isProgramer = True # This is a boolean Data type
sourceOfIncome = None #This is a none data type

print(f"My name is {name}. I am {age} years Old") # The f used here is called f string that is used to include variables in the string
print("And Yes i am learning to code as a beginner...")

# Basic Operations:
a = 5
b = 6

# 1. Addition --> +

sum = a+b
print(sum)


# 2. Division --> /

division = b/a
print(division)


# 3. Subtraction --> -

difference = b - a
print(difference)

# 4. Multiplication --> *

multiplication = a * b
print(multiplication)

# 5. Exponent --> **

exponent = a ** b
print(exponent)

# 6. Modulo --> %

modulo = b % a
print(modulo)

# Input statement:- This is used to take input from the user
name = input("Enter Your Name: ")
print(name) # By default it store data in the form of string so to make it other data type like integer we use typecasting

# TypeCasting:-
salary = int(input("Enter Your Salary: "))
print(salary)


# Conditional Statements:-

age = int(input("Enter Your Age: "))

if(age >= 18):
    print("You are an adult !")

elif(age>70):
    print("You are too Old !")


else:
    print("You are Young !")

# Day 01 Completed :)