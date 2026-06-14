"""
Problem 2. Write a program using a while loop that asks the user for a number
and prints a countdown from that number to zero.

"""

countdown = int(input("Enter the countdown value (max):"))

for c in range(countdown, -1,-1):
    print(c)