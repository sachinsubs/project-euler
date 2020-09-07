# Project Euler Problem 0001
# Multiples of 3 and 5

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# NOTES:
# - natural numbers: -2, -1, 0, 1, 2, ...

# Answer: 233168

lower_limit = 0
upper_limit = 1000

x = list(range(lower_limit, upper_limit, 1))  # create list of natural numbers, [lower_limit, upper_limit)

y = 0  # define variable to store sum of multiples

# print(x)

for el in x:
    if (el % 3 == 0) | (el % 5 == 0):
        y += el
        # print(el, y)

print(y)
