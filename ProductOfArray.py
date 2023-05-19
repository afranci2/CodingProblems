def productExceptSelf(nums):
    size = len(nums)
    leftProduct = [1]*size
    rightProduct = [1]*size

    for i in range(1,size):
        leftProduct[i] = leftProduct[i-1] * nums[i-1]
        rightProduct[size-i-1] = rightProduct[size-i] * nums[size-i]
        
        
    ans = []
    for i in range(size):
        ans.append(leftProduct[i] * rightProduct[i])
    return ans


print(productExceptSelf([2,1,3,4]))
nums = [2,1,3,4]
left = [1,2,2,6]
right=[12,12,4,1]

ans = [12,24,8,6]