class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #### 3 
        ### seen = {3: 0}
        #### rem = 7-3 

        ### 4 , seen = {3:0 , 4:1}
        ## rem = 7-4 = 3 in seen then return 0,1 
        seen = {}

        for i,n  in enumerate(nums):
            diff = target - n 
            if diff in seen:
                return [seen[diff],i]
            seen[n] = i 

        return            