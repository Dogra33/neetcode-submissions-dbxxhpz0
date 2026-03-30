class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_map, t_map = {}, {}

        for s_item in s:
            if s_item not in s_map:
                s_map[s_item] = 1
            else:
                s_map[s_item] += 1
        
        for t_item in t:
            if t_item not in t_map:
                t_map[t_item] = 1
            else:
                t_map[t_item] += 1

        print(s_map)
        print(t_map)

        if s_map == t_map:
            return True
        
        return False