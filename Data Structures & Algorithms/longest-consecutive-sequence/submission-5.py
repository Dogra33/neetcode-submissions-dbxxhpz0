class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) ==0:
            return 0
        nums = set(nums)
        nums = list(nums)
        nums.sort()
        count =1
        max_count = 1
        for index, num in enumerate(nums):
            if index+1 < len(nums) and num+1 == nums[index+1]:
                count+=1
                if max_count <= count:
                    max_count = count
            else:
                count = 1
        return max_count