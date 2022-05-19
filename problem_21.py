# Amicable numbers
# Problem 21

def proper_divisors(num):
    proper_divisors = []
    for n in range(num,1,-1):
        if num % n == 0:
            proper_divisors.append(num//n)
    return proper_divisors

num = 10000
amicable_numbers = 0
for n in range(1,num+1):
    a = sum(proper_divisors(n))
    b = sum(proper_divisors(a))
    if b == n and a != b:
        amicable_numbers += n

print(amicable_numbers)