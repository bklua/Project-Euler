# Circular primes
# Problem 35

import math
def is_prime(num):
    if num == 2:
        return True
    if num == 1 or num % 2 == 0:
        return False
    for n in range(3,int(math.sqrt(num))+1,2):
        if num % n == 0:
            return False
    return True

def is_circular_prime(str):
    if is_prime(int(str[::-1])):
        return True
    return False

result = 0
for n in range(2,1000001):
    if is_prime(n):
        if is_circular_prime(str(n)):
            result += 1
            #print(n)

print(result)