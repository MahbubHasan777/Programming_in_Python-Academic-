# Problem 5. Write a Python function that will take a list and print the counts of all distinct
# elements. Sample List : [10,20,30,30,30,30,20,40]
# Sample output : 10 => 1, 20 => 2, 30 => 4, 40 => 1

seq = [10,20,30,30,30,30,20,40]

def counter(seq):
    counter = {}

    for elem in seq:
        if elem in counter:
            counter[elem] += 1
        else:
            counter[elem] = 1
            
    for keys in counter:
        print(f"{keys} => {counter[keys]}", end=" ")
            
    
print(f"List: {seq}")
counter(seq)