# Pandigital multiples
# Problem 38

import math

def is_pandigital(nums):
    n_str = "".join(sorted(nums))
    if n_str == '123456789':
        return True
    return False

result = 0
attempt = int(math.sqrt(987654321))

for num in range(2,attempt):
    n_list = []
    for n in range(1,10):
        n_product = num * n
        n_list += list(str(n_product))
        if len(n_list) > 9:
            break
        if is_pandigital(n_list) and result <= int("".join(n_list)):
            result = int("".join(n_list))
            break

print(result)