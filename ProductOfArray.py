def productExceptSelf(nums):
    length = len(nums)
    left = [1]*length
    right = [1]*length
    for i in range(1,length):
        left[i] = nums[i] * left[i-1]
        right[length-i-1] = nums[length-i] * right[length-i]
    ans = []
    for i in range(length):
        print(ans)
        print(left)
        print(right)
       
        product1 = left[i]
        product2 = right[i]
        print(product1)
        ans.append(product1 * product2)
        print(ans)

productExceptSelf([1,2,3,4])