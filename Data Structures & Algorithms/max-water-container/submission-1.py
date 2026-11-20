class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        max_area = 0

        while i < j:
            width = j - i
            current_height = min(heights[i], heights[j])

            area = width * current_height

            if max_area < area:
                max_area = area

            if heights[i] < heights[j]:
                i = i + 1
            else:
                j = j - 1

        return max_area
