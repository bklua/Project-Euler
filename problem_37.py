# Truncatable primes 
# problem 37

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

def is_truncatable_prime_left(string):
    for i in range(len(string)):
        if not is_prime(int(string[:i+1])):
            return False
    return True
    
def is_truncatable_prime_right(string):
    for i in range(len(string)):
        if not is_prime(int(string[i:])):
            return False
    return True
    
n = 10
count = 0
result = 0
while count < 11:
    n += 1
    if is_prime(n):
        num_str = str(n)
        if is_truncatable_prime_left(num_str) and is_truncatable_prime_right(num_str):
            result += n
            count += 1
               
print(result)