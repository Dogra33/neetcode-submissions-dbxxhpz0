class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        mapper = {}
        for index, num in enumerate(nums):
            posiblity = nums[:index]+nums[index+1:]
            if num not in mapper:
                mapper[num] = [posiblity]

        res = []
        for key in mapper:
            new_list = []
            for lst in mapper[key]:
                p = 1
                for num in lst:
                    p *= num
                new_list.append(p)
            mapper[key] = new_list

        for num in nums:
            res.append(mapper[num][0])
            
        return res