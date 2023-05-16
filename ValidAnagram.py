def isAnagram(s,t):
    if len(s) != len(t):
        return False
    s = list(s)
    print(s)
    print(t)
    for i in range(len(t)):
        print(s)
        print(t)
        if t[i] not in s:
            return False
        s.remove(t[i])
    return True

print(isAnagram("aacc", "ccac"))