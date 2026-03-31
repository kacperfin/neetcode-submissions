class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        starting = set((num for num in nums if num-1 not in nums))
        max_length = 0
        for num in starting:
            i = num
            length = 0
            while i in nums:
                length += 1
                if length > max_length:
                    max_length = length
                i += 1
        return max_length