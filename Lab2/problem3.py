#Problem 3. Write a Program to check whether the given number is an even or odd number.


var = int(input("Enter the Number: "))

res = "even" if var % 2 == 0 else "odd"

print(f"{var} is a {res} number")