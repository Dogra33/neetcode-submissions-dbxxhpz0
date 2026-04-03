class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mapper = {}
        for i in range(0,len(numbers)):
            if numbers[i] not in mapper:
                mapper[numbers[i]] = i+1
        print(mapper)

        for num in numbers:
            res = []
            find = target - num 
            print(find)
            if find in mapper:
                res.append(mapper[num])
                res.append(mapper[find])
                return res
        
        return []