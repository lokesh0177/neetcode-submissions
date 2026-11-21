
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i] > 0:
                break

            elif i > 0 and nums[i] == nums[i-1]:
                continue

            l, h = i+1, len(nums)-1

            while l < h:
                sums = nums[i] + nums[l] + nums[h]

                if sums == 0:
                    res.append([nums[i], nums[l], nums[h]])
                    l, h = l+1, h-1

                    while l < h and nums[l] == nums[l-1]:
                        l += 1

                    while l < h and nums[h] == nums[h+1]:
                        h -= 1

                elif sums < 0:
                    l += 1

                else:
                    h -= 1

        return res
