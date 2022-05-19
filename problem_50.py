

import math
import time

def is_prime(num):
    if num == 2:
        return True
    if num == 1 or num % 2 == 0:
        return False
    for n in range(3,int(math.sqrt(num)+1),2):
        if num % n == 0:
            return False
    return True

def consecutive_prime(num):
    term_list = []
    for n in primes_list:
        term_list.append(n)
        if sum(term_list) == num:
            return num
        if sum(term_list) > num:
            break
    return 0

start = time.time()
primes_list = []

for n in range(2,1000000):
    if is_prime(n):
        primes_list.append(n)
        
result = 0

for n in primes_list:
    num = consecutive_prime(n)
    if len(str(num)) >= len(str(result)):
        result = num
                 
print(result)           
print(time.time() - start)