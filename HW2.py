# HW2.py
# Author: Nate Harris


# Question 1:
# Write some code that prompts the user for their age. Depending on the input:

age = int(input("Enter your age: "))    

# If the age is less than 13, print "You are a child."
# If the age is between 13 and 19, print "You are a teenager."
# If the age is 20 or older, print "You are an adult."

if age < 13:
    print("You are a child.")
elif age >= 13 and age < 20:
    print("You are a teenager.")
else:
    print("Governtment says you're an adult, your firends, well. \n")


# Question 2:
# Write some code to display the following pattern using a for or while loop:
# 1
# 12
# 123
# 1234
# 12345

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end='')
        if j == i:
            break
    print()

# Question 3:
# Write a Python program that prompts the user to input 10 numbers. After all the numbers are inputted, the program should display:

print("\nEnter 10 numbers:")

largest = smallest = 0
sum = 0
count = 1

while count <= 10:
    number = int(input("Enter number " + str(count) + ": "))
    if count == 1:
        largest = smallest = number
    if number > largest:  
        largest = number
    if number < smallest:
        smallest = number
    count += 1
    sum += number
    average = sum / 10
else:
        print("\nLargest number is:", largest)
        print("Smallest number is:", smallest)
        print("Average is:", average,)

# Question 4:
# Vowel Counter - Write some code that prompts the user to enter a string. The program should then display the number of vowels in the string. IE. If the user enters "Hello World", the program should display 3.
# the vowels are a, e, i, o, u
# Hint: convert the string to lowercase and use a for loop with a counter variable and an if statement

string = input("\nEnter a string: ")  
string = string.lower()
vowel_count = 0
for i in string:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u': 
        vowel_count += 1
print("\nNumber of vowels: ", vowel_count,)
print("String value lower cased is:" , string)


