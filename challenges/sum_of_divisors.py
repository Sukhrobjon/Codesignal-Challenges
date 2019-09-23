import math


def sum_of_divisors_v1(n):
    """Naive version: Find the sum of all divisors of a given integer."""
    sum_div = 0
    for i in range(1, n+1):
        # check if n is divisible by current number from 1 to n inclusive
        if n % i == 0:
            sum_div += i
    return sum_div


def sum_of_divisors_v2(n):
    """Find the sum of all divisors of a given integer.
    NOTE: If we look carefully, all the divisors are present in pairs. For
    example if n = 100, then the various pairs of divisors are: (1,100),
    (2,50), (4,25), (5,20), (10,10).
    resource: https://www.geeksforgeeks.org/find-divisors-natural-number-set-1/
    """
    result = 0
    i = 1
    # loop through only sqrt(n) times
    while i <= math.sqrt(n):
        # we want to find the pair of divisors
        if n % i == 0:
            # if pairs are equal, add to result only one of them
            if i == (n//i):
                result += i
            # else, add both pairs of divisors to the result
            else:
                result += i + (n//i)
        i += 1
    return result


n = 12
print(sum_of_divisors_v2(n))
