n=0

num=0
total=0
while total != n:
    total = 2**num
    num += 1
    if (num == 2**10 or n==0):
        print(False)
        break
print(True)