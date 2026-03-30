# -> length of set should be same.
# -> both sets should be same.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        sets = {}

        for word in strs:
            # Use sorted word as key (duplicates preserved)
            x = ''.join(sorted(word))

            if x not in sets:
                sets[x] = [word]
            else:
                sets[x].append(word)

        # Convert dictionary values to list of lists
        for value in sets.values():
            result.append(value)

        return result