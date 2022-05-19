# Distinct powers 
# Problem 29

size = 100
num_list = []

for a in range(2,size+1):
    for b in range(2,size+1):
        num_list.append(a**b)
 
num_list = set(num_list)

print(len(num_list))