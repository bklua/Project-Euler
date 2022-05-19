# Double-base palindromes 
# Problem 36

def is_palindrome(str):
    if str == str[::-1]:
        return True
    return False

palindromic_base2 = 0
palindromic_number = 0

for n in range(1,int(1.0e6)):
    if is_palindrome(str(n)):
        palindromic_base2 = format(n, 'b')
        if is_palindrome(str(palindromic_base2)):
            palindromic_number += n
            
print(palindromic_number)