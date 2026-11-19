class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0

        for i in nums:
            if (i-1) not in numset:
                count = 1
                current = i

                while (current+1) in numset:
                    current+=1
                    count+=1
                longest = max(count,longest)
        return longest
