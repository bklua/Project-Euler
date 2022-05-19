

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

i = 0
n = 1
while i <= 10001:
    n += 1
    if is_prime(n):
        i += 1

print(n)