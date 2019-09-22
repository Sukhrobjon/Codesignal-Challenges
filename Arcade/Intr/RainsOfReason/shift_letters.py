import string


def alphabetic_shift(input_string):
    """
    Given a string, function replaces each of its characters by the next
    one in the English alphabet; i.e. replace a with b, replace b with c, etc
    (z would be replaced by a).
    """
    output_list = list(input_string)
    print(output_list)
    for i in range(len(output_list)):
        if output_list[i] == 'z':
            output_list[i] = 'a'
        else:
            output_list[i] = chr(ord(output_list[i]) + 1)
    return "".join(output_list)

s = 'crazy'
print(alphabetic_shift(s))
