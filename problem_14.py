# Longest Collatz sequence
# Problem 14

def collatz_sequence(nums):
    collatz_sequence = [nums]
    while nums != 1:   
        if nums % 2 != 0:
            nums = 3 * nums + 1
            collatz_sequence.append(nums)
        nums = nums // 2
        collatz_sequence.append(nums)
    return collatz_sequence

longest_collatz_sequence = 0
pre_longest = 0
cur_longest = 0
num = 1000000

for n in range(1,num):
    pre_longest = len(collatz_sequence(n))
    if  pre_longest >= cur_longest:
        longest_collatz_sequence = n
        cur_longest = pre_longest
    
print(longest_collatz_sequence)