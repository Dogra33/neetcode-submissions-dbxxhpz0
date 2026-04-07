class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = set()
        left = 0
        max_len = 0

        for right in range(0, len(s)):
            print("--> ", s[right])
            while s[right] in res:
                print("Removing elemt: ", s[right])
                res.remove(s[left])
                left+=1
            res.add(s[right])
            max_len = max(max_len, right-left+1)
            print(res)
            print()        
        return max_len

