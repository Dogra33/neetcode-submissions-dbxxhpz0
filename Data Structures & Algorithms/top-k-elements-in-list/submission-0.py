class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapper = {}
        res = []
        for num in nums:
            if num not in mapper:
                mapper[num] = 1
            else:
                mapper[num] +=1
        print(mapper)
        sorted_map = sorted(mapper, key=mapper.get)        
        print(sorted_map)
        return sorted_map[-k:]