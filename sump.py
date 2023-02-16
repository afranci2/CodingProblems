nums = [1,2,3,4]
numtrack=0
for i in range(min(nums), max(nums)):
    numtrack^=i
    i+=1
print(numtrack)
for num in nums:
    numtrack^=num
    if numtrack==0:
        print(True)
    print(numtrack)