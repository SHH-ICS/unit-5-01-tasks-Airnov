# Create a program that will accept the two legs of a right-angle triangle, a and b, and display the length of the hypotenuse, c. 
# Remember to use prompts for the input and labels for the output. Use the formula a2 + b2 = c2 to calculate your answer.
import math 

sidea = float(input("What is the lenght a side a of the right angle triangle"))
sideb = float(input("What is the lenght a side b of the right angle triangle"))
sidec = math.sqrt(sidea**2+sideb**2)
print(f"The length of the side c is {sidec}")
