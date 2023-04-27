# Create a program that accepts 2 numbers from the user. 
# Your program will output a random number between the range given by the user.

import random

a = int(input("input a random whole number: "))
b = int(input("input another random whole number: "))
num1 = random.randint(a, b)
print(num1) 
