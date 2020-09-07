# Project Euler Problem 0004
# Largest palindrome product

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# NOTES:
# - https://en.wikipedia.org/wiki/Palindrome
# - https://www.w3schools.com/python/python_howto_reverse_string.asp

# Answer: 906609

# initialize variables
x_max = 999
y_max = 999
max_palindrome = 0

def is_palindrome(i, j):
    k = str(i * j)

    if k == k[::-1]:
        return True
    else:
        return False


for i in range(x_max, 0, -1):
    for j in range(y_max, 0, -1):
        if is_palindrome(i, j) == True:
            max_palindrome = max(max_palindrome, i * j)

print(max_palindrome)
