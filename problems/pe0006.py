# Project Euler Problem 0006
# Sum square difference

# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
# 3025 - 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# NOTES:
# - 

# Answer: 25164150

def square_list(x):
    return [el ** 2 for el in x]

# initialize variables
lower_limit = 1
upper_limit = 101

x = list(range(lower_limit, upper_limit, 1))  # create list of natural numbers, [lower_limit, upper_limit)


print((sum(x) ** 2) - sum(square_list(x)))
