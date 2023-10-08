# HW1.py
# Author: Nate Harris

# Question 1:
# Print Hello World like we did in class
print("Hello World")


# Question 2:
# Print the following:
# Your name
print("Nate")


# Your age
print(38)

# Your favorite color
print("Blue")


# Your favorite animal
print("Dog")


# Question 3:
# Create a variable called "myName" and set it equal to your name
name = "Nate"


# Create a variable called "myAge" and set it equal to your age
age = 38


# Create a variable called "myColor" and set it equal to your favorite color
my_color = "Blue"

# Create a variable called "myAnimal" and set it equal to your favorite animal
my_animal = "Dog"


# Print the following:
# Hello, my name is <myName>
print("Hello, my name is " + name)

# I am <myAge> years old
print("I am " + str(age) + " years old")

# My favorite color is <myColor>
print("My favorite color is " + my_color)

# My favorite animal is <myAnimal>
print("My favorite animal is a " + my_animal)


# Question 4:
# Calculate the following and print the result:
# 2 + 2

print(2 + 2)

# 3 * 4

print(3 * 4)

# 5 - 6

print(5 - 6)

# 8 / 2

print(8 / 2)

# Question 5:
# Create a variable called "num1" and set it equal to 2

num1 = int(2)

# Create a variable called "num2" and set it equal to 3

num2 = int(3)

# Create a variable called "num3" and set it equal to 4

num3 = int(4)

# Create a variable called "num4" and set it equal to 5

num4 = int(5)

# Calculate the following and print the result:

# num1 + num2

print(num1 + num2)

# num3 * num4

print(num3 * num4)

# num4 - num1

print(num4 - num1)  

# num2 / num1

print(num2 / num1)

# Question 6: Write a program that asks the user for their name and then prints the following:

name = input("What is your name? \n")

print("\nHello " + name + "," " please enter three numbers with decimals. \n")

# The program should then ask the user for three numbers (floats) and print the following:

num1 = float(input("Enter first number: \n"))
num2 = float(input("Enter second number: \n"))
num3 = float(input("Enter third number: \n"))

# 2. The product of the three numbers is <product>

product = num1 * num2 * num3
product = float(product)

print("\nThe product of your numbers is: ", product)

# 3. round the three numbers to the nearest integer and print the sum of the three rounded numbers divided by 3 

num1 = round(num1,0)
num2 = round(num2,0)
num3 = round(num3,0)

print("\nThe rounded numbers are: ", num1, num2, num3)

# 4. The average of the three numbers is <average>

average = round((num1 + num2 + num3) / 3, 2)
print("\nThe average of your numbers is: ", average)

# Question 7: Ask the user for an input of a symbol (in the example its *)     
# Print a diamond of the symbol that looks like the following. Include the spaces and the | character. 
# Hint: the print("symbol", end="") with \t and \n characters will be useful here.

symbol = input("\nEnter a symbol: ")
symbol2 = input("Enter another but different symbol: ")
symbol3 = input("Last time, another but different symbol: ") 

print("\n", symbol2, " " * 8, symbol, "     ", symbol3, "\n", symbol2, " " * 6, symbol, symbol, symbol, "   ", symbol3, 
      "\n", symbol2, " " * 4, symbol, symbol, symbol, symbol, symbol, " ",symbol3, 
      "\n", symbol2, " " * 2, symbol, symbol, symbol, symbol, symbol, symbol, symbol, symbol3, 
      "\n", symbol2, " " * 4, symbol, symbol, symbol, symbol, symbol, " ", symbol3, 
      "\n", symbol2, " " * 6, symbol, symbol, symbol, "   ", symbol3, "\n", symbol2, " " * 8, symbol, "     ", symbol3, "\n")    

#    *     |
#   ***    |
#  *****   |
# *******  |
#  *****   |
#   ***    |
#    *     |
