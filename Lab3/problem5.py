N = int(input("Enter N: "))

fib = [0, 1]

while fib[-1] + fib[-2] < N:
    fib.append(fib[-1] + fib[-2])

for num in fib:
    print(num, end=" ")