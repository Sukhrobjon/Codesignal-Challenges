def arithmetic_progression(el_1, el_2, n):
    """Finds the nth element of Given the first two elements of
    an arithmetic progression.
    NOTE: nth term for arithmetic progression is a sub n = (n-1)*d + a
    where n is the nth term, d is difference, a is the first element of
    the arithmetic progression.
    """
    a = el_1
    d = el_2 - el_1
    return (n-1) * d + a
