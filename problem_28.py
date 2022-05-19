# Number spiral diagonals
# Problem 28

size = 1001
l =[]
for n in range(size):
    l.append([0]*size)

def fill_num(r,c,m,limit):
    if m <= limit:
        l[r][c] = m
     
num = size ** 2
i = 0
m = 1
r = size // 2
c = size // 2

l[r][c] = m

while m <= num:
    for n in range(1,2*i+2):
        c += 1
        m += 1
        fill_num(r,c,m,num)
        
    for n in range(1,2*i+2):
        r += 1
        m += 1
        fill_num(r,c,m,num)
        
    for n in range(1,2*i+3):
        c -= 1
        m += 1
        fill_num(r,c,m,num)
        
    for n in range(1,2*i+3):
        r -= 1
        m += 1
        fill_num(r,c,m,num)
            
    if m > num:
        break
            
    i += 1    

result = 0
for n in range(size):
    result += l[n][n]
    result += l[n][size-n-1]
    
print(result - 1)