class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0 
        end = len(numbers) - 1
        currentSum = 0 
        while start < end:
            currentSum = numbers[start] + numbers[end]
            if currentSum == target:
                return [start+1,end+1]
            if currentSum > target:
                end -= 1 
            else:
                start +=1 
        return []
