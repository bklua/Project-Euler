# Lexicographic permutations
# Problem 24

import itertools

n = list(itertools.permutations(range(10), 10))
print(n[999999])