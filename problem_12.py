

from functools import reduce

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

n = 7
i = []

while len(i) <= 500:
    n += 1
    triangle_numbers = n * (n+1) // 2
    i = factors(triangle_numbers)

print(len(i)-1)
print(triangle_numbers)