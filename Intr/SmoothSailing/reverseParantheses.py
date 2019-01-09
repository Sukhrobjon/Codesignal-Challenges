def reverseParentheses(s):
    between = s[s.find("(")+1:s.find(")")]
    return between[::-1]



 
# voted #1 solution
def reverseParenthesesOne(s):
    for i in range(len(s)):
        if s[i] == "(":
            start = i
        if s[i] == ")":
            end = i
            return reverseParentheses(s[:start] + s[start+1:end][::-1] + s[end+1:])
    return s


s = "a(bcdefghijkl(mno)p)q"
print(reverseParenthesesOne(s))
