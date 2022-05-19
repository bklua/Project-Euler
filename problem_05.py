

def is_divided_by_1_to_20(num):
    for n in range(1,21):
        if num % n != 0:
            return False
    return True

i = 2
while True:
    if is_divided_by_1_to_20(i):
        print(i) 
        break
    i += 2   