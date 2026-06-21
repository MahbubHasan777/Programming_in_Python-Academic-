# Problem 2. Write a Python program to count the frequency of values in a dictionary. Original Dictionary: {'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}Count the frequency of the said dictionary: Counter({10: 2, 40: 2, 20: 2, 70: 1, 80: 1})


dict = {
    "V": 10,
    "VI": 10,
    "VII": 40,
    "VIII": 20,
    "IX": 70,
    "X": 80,
    "XI": 40,
    "XII": 20,
}

Counter = {}

for keys in dict:
    if dict[keys] in Counter.keys():
        Counter[dict[keys]] += 1
    else:
       Counter[dict[keys]] = 1
        
        
print(f"dict{dict}")
print(f"Counter{Counter}")