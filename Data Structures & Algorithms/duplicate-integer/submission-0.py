class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = {}

        for num in nums:
            if num not in dup:
                dup[num] = 1
            elif num in dup:
                dup[num] += 1
        
        for key, value in dup.items():
            if value > 1:
                return True

        return False
