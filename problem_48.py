

result = 0

for n in range(1,1001):
    result += n**n
    
result = str(result)  
print(result[-10:])