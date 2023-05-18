def topKFrequent(nums,k):
    numbers = {}
    list_of_nums=[]
    for i in range(len(nums)):
        if nums[i] not in numbers:
            numbers[nums[i]] = 1
        else:
            numbers[nums[i]] += 1
    for i in range(k):
        some = max(numbers, key=numbers.get)
        list_of_nums.append(some)
        del numbers[some]
    return list_of_nums

print(topKFrequent([4,1,-1,2,-1,2,3],2))