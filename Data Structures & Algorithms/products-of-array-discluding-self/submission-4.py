class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        indexes_of_0 = []

        for i in range(len(nums)):
            if nums[i] == 0:
                indexes_of_0.append(i)

        if len(indexes_of_0) >= 2:
            return [0] * len(nums)
        elif len(indexes_of_0) == 1:
            val = 1
            for i in range(len(nums)):
                if i != indexes_of_0[0]:
                    val *= nums[i]
            for i in range(len(nums)):
                if i != indexes_of_0[0]:
                    nums[i] = 0
                else:
                    nums[i] = val
            return nums
        else:
            val = 1
            for i in range(len(nums)):
                val *= nums[i]
            for i in range(len(nums)):
                nums[i] = val // nums[i]
            return nums