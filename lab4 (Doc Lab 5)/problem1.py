# Problem 1. Write a Python program to combine two dictionaries by adding values for commonkeys. d1 = {'a': 100, 'b': 200, 'c': 300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})


d1 = {"a": 50, "b": 100, "c": 70, "d": 120}

d2 = {"a": 50, "b": 100, "e": 70, "d": 120}

Counter = {}

for i in d1.keys():
    Counter[i] = d1[i]

for i in d2.keys():
    if i in Counter.keys():
        Counter[i] += d2[i]

    else:
        Counter[i] = d2[i]
        
print(f"Dictionary 1{d1}")
print(f"Dictionary 2{d2}")
print(f"Counter{d2}")