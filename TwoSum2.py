def twoSum(numbers, target):
    valid_index=[]
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            print(numbers[i], numbers[j])

            if (numbers[i]+numbers[j]) == target and i != j:
                valid_index.append(i+1)
                valid_index.append(j+1)
                return valid_index



print(twoSum([1,2,3,4,4,9,56,90], 8))