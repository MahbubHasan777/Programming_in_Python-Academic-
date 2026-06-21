# Problem 6. Write a Python lambda function to find if a given string starts with a given sub-stringusing Lambda.

def isStartWith():
    s = input("Enter the sting: ")
    sub = input("Enter the sting: ")
    starts_with = lambda s, sub: s.startswith(sub)
    
    if starts_with(s, sub):
        print("string starts with a given sub-stringusing Lambda")
    else:
        print("string doesnot start with a given sub-stringusing Lambda")
    

isStartWith()