def twoSum(numbers, target):
    class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans = []
        left = 0
        right = len(numbers)-1
        for i in range(right):
            number = numbers[left] + numbers[right]
            if number > target:
                right = right - 1
            elif number<target:
                left = left+1

        ans.append(left+1)
        ans.append(right+1)

        return ans
        
print(twoSum([1,2,3,4,4,9,56,90], 8))