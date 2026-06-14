#Problem 4. Take a character as input and determine whether it is a vowel.
# Therefore, print an appropriate message (vowel/not vowel).


#Problem 3. Write a Program to check whether the given number is an even or odd number.


var = input("Enter the charecter: ")

res = "vowel" if var in "AEIOUaeiou" else "not vowel"

print(f"{var} is a {res} charecter")
