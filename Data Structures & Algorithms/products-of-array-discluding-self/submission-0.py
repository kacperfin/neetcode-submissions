class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        indexes_of_0 = []

        for i in range(len(nums)):
            if nums[i] == 0:
                indexes_of_0.append(i)

        if len(indexes_of_0) >= 2:
            return [0] * len(nums)
        elif len(indexes_of_0) == 1:
            l = [0] * len(nums)
            val = 1
            for i in range(len(nums)):
                if i != indexes_of_0[0]: # if not the 0
                    val *= nums[i]
            l[indexes_of_0[0]] = val
            return l
        else:
            val = 1
            for i in range(len(nums)):
                val *= nums[i]
            l = [val] * len(nums)

            for i in range(len(nums)):
                l[i] //= nums[i]

            return l