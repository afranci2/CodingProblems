def isValid(s):
    stack=[]
    for i in range(len(s)):
        stack.append(s[i])
    
    print(stack)
    return True

print(isValid("()[]{}"))