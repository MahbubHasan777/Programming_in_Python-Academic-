import math

"""
Problem 2. Write a program to compute the distance between two points, taking input from the user.
[Distance formula = d=√((x2-x1)²+(y2-y1)²)] 
"""

x1 = float(input("Input co-ordinate of x1: "))
x2 = float(input("Input co-ordinate of x2: "))
y1 = float(input("Input co-ordinate of y1: "))
y2 = float(input("Input co-ordinate of y2: "))

distance = math.sqrt((x1-x2)**2+(y1-y2)**2)

print(f"distance is: {math.floor(distance * 100) / 100}")
