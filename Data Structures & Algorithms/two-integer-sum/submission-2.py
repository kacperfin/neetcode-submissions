class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, num in enumerate(nums):
            hashmap[num] = index

        for num_index, num in enumerate(nums):
            looking_for = target - num
            if looking_for in hashmap:
                looking_for_index = hashmap[looking_for]
                if num_index == looking_for_index:
                    continue
                return [num_index, looking_for_index]