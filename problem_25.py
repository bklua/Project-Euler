# 1000-digit Fibonacci number
# Problem 25

def fabonacci_term(limit):
    fab = [1]
    f1 = 0
    i = 0
    while True:
        fab.append(fab[i]+f1)
        f1 = fab[i]
        if len(str(f1)) == limit:
            return i+1
        i += 1
        
first_term_contain_1000_digits = fabonacci_term(1000)
print(first_term_contain_1000_digits)