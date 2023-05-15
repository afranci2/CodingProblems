
def plusOne(digits):
    some = []
    new_array=[]
    for i in range(len(digits)):
        letter = str(digits[i])
        some.append((letter))
    some = str(int("".join(some))+1)
    for i in range((len(some))):
        new_array.append(int(some[i]))
    print(new_array)


plusOne([1,2,3])