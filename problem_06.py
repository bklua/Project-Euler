

sum_of_squares = 0
squares_of_sum = 0

for n in range(1,101):
    sum_of_squares += n**2
    squares_of_sum += n
    
print(squares_of_sum**2 - sum_of_squares)