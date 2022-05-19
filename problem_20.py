#Factorial digit sum
#Problem 20

result = 1
for n in range(2,101):
    result *= n
    
print(sum(map(int,str(result))))