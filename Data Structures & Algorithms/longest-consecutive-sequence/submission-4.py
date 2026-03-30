class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) ==0:
            return 0
        nums = set(nums)
        print(nums)
        nums = list(nums)
        nums.sort()
        print(nums)

        count =1
        max_count = 1
        for index, num in enumerate(nums):
            print("Num = ", num)
            print("Next num should: ",num+1)
            if index+1 < len(nums) and num+1 == nums[index+1]:
                count+=1
                print("Count: ", count)
                print("Max : ", max_count)
                if max_count <= count:
                    max_count = count
                    print("New MAx: ", max_count)
                    print()
            else:
                count = 1
                print()

        return max_count