# Problem 4. Write a Python function that takes a list and returns a new list with distinct elementsfrom the list. Sample List : [1,2,3,3,3,3,4,5]
# Sample output : [1, 2, 3, 4, 5]

listData = [1,2,2,3,3,3,3,4,5]

def toSet(seq):
    return (list(set(seq)))
print(f"List: {listData}")
print(f"Unique List: {toSet(listData)}")