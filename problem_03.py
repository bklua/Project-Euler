

import math

def is_prime(num):
    if num == 2:
        return True
    if num == 1 or num % 2 == 0:
        return False
    for n in range(3,int(math.sqrt(num)+1),2):
        if num % n == 0:
            return False
    return True

def largest_prime_factor(num):
    result = 0
    for n in range(3,int(math.sqrt(num))):
        if is_prime(n) and num % n == 0 :
            result = n
    return result    
    
print(largest_prime_factor(600851475143))