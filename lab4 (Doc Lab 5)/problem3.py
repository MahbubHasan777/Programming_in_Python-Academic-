# Problem 3. Write a Python function that checks whether a passed string is a palindrome.

def isPalidrom():
    str = input("Enter the String: ")
    checker = True
    
    length = len(str)
    
    for i in range(int(length/2)):
        if str[i] != str[length-i-1]:
            checker = False
        
    return "Palidrom" if checker == True else "Not Palidrom"

print(isPalidrom())