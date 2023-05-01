# Create a program that will ask the user an addition question. 
# The program will generate two random numbers between 1 and 100, and display them as an addition question with appropriate prompts.

import random 

num1 = random.randint(1, 100)
num2 = random.randint(1, 100)

print ("Add these 2 numbers")
a = int(input(str(num1) + " + " + str(num2) + " = ")) 

if a == num1 + num2:
    print("Correct")
else:
    print("Wrong")

