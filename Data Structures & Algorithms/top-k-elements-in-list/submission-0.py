class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        frequent = {}

        for i in nums:
            if i in frequent:
                frequent[i] += 1
            else:
                frequent[i] = 1

        sorted_nums = sorted(frequent, key=frequent.get, reverse=True)

        return sorted_nums[:k]