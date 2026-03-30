class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, num in enumerate(nums):
            hashmap[num] = index

        for num_index, num in enumerate(nums):
            looking_for = target - num
            if looking_for in hashmap and hashmap[looking_for] != num_index:
                return [num_index, hashmap[looking_for]]