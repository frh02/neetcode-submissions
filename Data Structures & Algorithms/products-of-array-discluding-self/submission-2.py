class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix 
        # suffix 
        # adding 
        n = len(nums)
        output = [1]*n

        left_product = 1
        for i in range(n):
            output[i] = left_product 
            left_product *= nums[i]

        right_product = 1 
        for i in reversed(range(n)):
            output[i] *= right_product 
            right_product *=nums[i]
        return output 