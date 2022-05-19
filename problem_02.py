

result = 0
n1 = 0
n2 = 1

for n in range(4000):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    if n3 < 4000000 and n3 % 2 == 0:
        result += n3

print(result)