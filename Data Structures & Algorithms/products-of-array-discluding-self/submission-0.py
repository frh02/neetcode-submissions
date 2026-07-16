class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix 
        # suffix 
        # adding 
        res = [0]*len(nums) 
        
        for i in range(len(nums)):
            prodSum = 1 
            for j in range(len(nums)):

                if i == j:
                    continue
            
                prodSum *= nums[j]
            
            res[i] = prodSum
        return res 
