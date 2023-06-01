def isPalindrome(s):
    new_s=[]
    for i in range(len(s)):
        if s[i].isalnum()==True:
            new_s.append(s[i].lower())
    new_string = "".join(new_s)

    for i in range(len(new_string)):
        left = i
        right = len(new_string)-1-i
        if new_string[left] != new_string[right]:
            return False
    return True
print(isPalindrome(""))