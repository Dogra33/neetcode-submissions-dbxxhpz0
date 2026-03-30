class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}
        for i, num in enumerate(nums):
            tgt = target - num
            if tgt in index_map:
                return [index_map[tgt],i]
            index_map[num] =i
