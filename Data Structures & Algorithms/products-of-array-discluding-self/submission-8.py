class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        counter = 1
        for i in range(len(nums)):
            result[i] *= counter
            counter *= nums[i]
        
        counter = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= counter
            counter *= nums[i]

        return result
