def evenDigitsOnly(n):
    digits = [int(x) for x in str(n)]
    return all(item % 2 == 0 for item in digits)

n = 248632
print(evenDigitsOnly(n))