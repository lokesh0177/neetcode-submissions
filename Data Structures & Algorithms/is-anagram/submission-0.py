class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashdict = {}

        for i in s:
            if i in hashdict:
                hashdict[i] += 1
            else:
                hashdict[i] = 1

        for i in t:
            if i not in hashdict or hashdict[i] == 0:
                return False

            hashdict[i] -= 1

        return True