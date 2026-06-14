# Problem 4. Find the sum of all the primes below 1000.


def isPrime(num):
    for i in range(2, int((num/2))+1, 1):
        if(num % i == 0):
            return False
    return True

prime_list = []

for i in range(2,1001,1):
    if(isPrime(i)):
        prime_list.append(i)
        
        
print(f"Sum of prime numbers from 1 to 1000: {sum(prime_list)}")