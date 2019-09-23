import math


def sum_of_divisors(n):
    """Find the sum of all divisors of a given integer."""
    result = 0
    i = 1
    sum_l = []
    while i <= math.sqrt(n):
        if n % i == 0:
            result += i
            sum_l.append(i)
        else:
            result += i + (n//i)
            sum_l.append(i)
            sum_l.append(n//i)
        i += 1
    print(sum_l)
    return result


def sum_of_divisors_v2(n):
    """Find the sum of all divisors of a given integer."""
    result = 0
    i = 1
    while i <= math.sqrt(n):
        if n % i == 0:
            if i == (n//i):
                result += i
                # print(f"divisor: {i}")
            else:
                result += i + (n//i)
        i += 1
    return result


n = 12
print(sum_of_divisors_v2(n))


# method to print the divisors
def printDivisors(n):
    # Note that this loop runs till square root
    i = 1
    sum_l = []
    while i <= math.sqrt(n):

        if (n % i == 0):

            # If divisors are equal, print only one
            if (n / i == i):
                print(i)
                sum_l.append(i)
            else:
                # Otherwise print both
                print(i, n//i)
                sum_l.append(i)
                sum_l.append(n//i)
        i += 1
    return sum_l


# Driver method
# print("The divisors of 100 are: ")
# print(printDivisors(12))
