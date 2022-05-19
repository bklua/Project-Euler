

def check_Hexagonal_number(pos, match):
    n = pos[0]
    while n*(2*n-1) < match[2]:
        n += 1
    pos[0] = n
    match[0] = n*(2*n-1)
        
def check_pentagonal_number(pos, match):
    n = pos[1]
    while n*(3*n-1)//2 < match[0]:
        n += 1 
    pos[1] = n
    match[1] = n*(3*n-1)//2
    
def check_triangle_number(pos, match):
    n = pos[2]
    while n*(n+1)//2 < match[1]:
        n += 1
    pos[2] = n  
    match[2] = n*(n+1)//2

pos = [2,2,2]
match = [0,0,0]
count = 0
result = 0

while count < 2:   
    check_pentagonal_number(pos, match)
    check_triangle_number(pos, match)
    check_Hexagonal_number(pos, match)
    
    if match[0] == match[1] == match[2]:
        pos[0] += 1
        count += 1
        result = match[0]
        match[0] = 0
        
print(result)