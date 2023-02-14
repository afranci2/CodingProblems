nums = [1,3,5,6]
target = 5
low = 0
high = len(nums)-1
mid = 0
num_position = 0

while low <= high:
    mid = (high+low)//2
    if nums[mid] < target:
        low = mid+1
        num_position = mid+1
    elif nums[mid] > target:
        high = mid - 1
        num_position = mid
    else:
        print(mid)
print(num_position)
