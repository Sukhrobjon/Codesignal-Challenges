def reverseParentheses(s):
    between = s[s.find("(")+1:s.find(")")]
    return between[::-1]

s = "a(bcdefghijkl(mno)p)q"
s2 = "foo(bar(baz))blim"
s3 = '(bar)'
print(reverseParentheses(s2))

def reverse_parantheses(s):
    """ 
        Reverses characters in (possibly nested) 
        parentheses in the input string.
    """
    # traverse the string
    # once "(" found 
    for i in len(s):
        if s[i] == '(':
            start = i
        if s[i] == ')':
            end = i
        
    return s[end:start]
        