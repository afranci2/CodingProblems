def longestConsecutive(arr):
    numSet = set(arr)
    longest = 0
    print(numSet)
    min_val = min(arr)
    max_val = max(arr)
    range_size = max_val - min_val + 1
    count = [0] * range_size
    sorted_array = [0] * len(arr)
    count2=[0]
    valid=True
    for num in arr:
        count[num - min_val] += 1

    for i in range(1, range_size):
        count[i] += count[i - 1]

    for num in reversed(arr):
        index = count[num - min_val] - 1
        sorted_array[index] = num
        count[num - min_val] -= 1
    print(sorted_array)
    for i in range(1,len(sorted_array)):
        print(count2)
        if sorted_array[i]==sorted_array[i-1]+1 or sorted_array[i]==sorted_array[i-1]-1:
            count2[len(count2)-1]+=1
            valid=True

        elif valid==True:
            count2.append(1)
    print(count2)
    return max(count2)


print(longestConsecutive([100,4,200,1,3,2]))
print(longestConsecutive([1,2,0,1]))
print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))