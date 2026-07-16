class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] ==nums[j]:
                    return True 


        # nums = [1,2,3,4] - i=0, j =0 


        return False
