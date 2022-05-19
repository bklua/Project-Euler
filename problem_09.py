

import math

def pythagorean_triplet_product(num):
    for a in range(2,num):
        for b in range(a+1,num):
            c = math.sqrt(a**2 + b**2)
            if c % int(c) == 0.0 and int(a + b + c) == 1000:
                return int(a * b * c)
    
print(pythagorean_triplet_product(1000))