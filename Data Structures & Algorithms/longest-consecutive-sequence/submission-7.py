class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)

        longest = 0

        for num in s:
            if num-1 not in s:
                i = num
                length = 0
                while i in nums:
                    length += 1
                    i += 1
                if length > longest:
                    longest = length

        return longest