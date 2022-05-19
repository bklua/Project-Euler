# Sub-string divisibility
# Problem 43

import itertools

n_list = list(range(10))
result = 0

for i in itertools.permutations(n_list,10):
    if ((i[1]*100 + i[2]*10 + i[3]) % 2 == 0 and
     (i[2]*100 + i[3]*10 + i[4]) % 3 == 0 and
     (i[3]*100 + i[4]*10 + i[5]) % 5 == 0 and
     (i[4]*100 + i[5]*10 + i[6]) % 7 == 0 and
     (i[5]*100 + i[6]*10 + i[7]) % 11 == 0 and
     (i[6]*100 + i[7]*10 + i[8]) % 13 == 0 and
     (i[7]*100 + i[8]*10 + i[9]) % 17 == 0):
        result += int("".join(map(str,i)))
        
print(result)