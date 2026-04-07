class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        left = 0
        right = left+1
        subs = [s[left]]
        max_len = 0

        while right < len(s):
            if s[left] != s[right] and s[right] not in subs:
                # print(f"Comparing {s[right]} from {subs}")
                subs.append(s[right])
                # print("-> ", subs)
                max_len = max(max_len, len(subs))
                right +=1
            elif s[right] in subs:
                # print("dup found ")
                max_len = max(max_len, len(subs))
                # print("Max Len = ", max_len)
                left+=1
                right = left+1
                subs = [s[left]]
                # print("New sub = ", subs)
            # print()

        return max_len

