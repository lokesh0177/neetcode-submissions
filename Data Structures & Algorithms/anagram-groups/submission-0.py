from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)
        result = []

        for s in strs:
            sorted_s = tuple(sorted(s))
            anagram[sorted_s].append(s)

        for k,v in anagram.items():
            result.append(v)

        return result

