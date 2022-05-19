

def is_palindrome(str):
    if str == str[::-1]:
        return True
    return False

def largest_palindrome(num1, num2):
    largest_palindrome = 0
    for n1 in range(num1,100,-1):
        for n2 in range(num2,100,-1):
            if is_palindrome(str(n1 * n2)) and largest_palindrome < n1 * n2:
                largest_palindrome = n1 * n2
    return largest_palindrome

print(largest_palindrome(999,999))