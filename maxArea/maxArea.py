class Solution:
    def maxArea(self, height: List[int]) -> int:
        first = 0
        last = len(height) - 1
        max_area = 0
        while first < last:
            height1 = height[first]
            height2 = height[last]
            area = min(height1, height2) * (last - first)
            max_area = max(max_area, area)
            if height1 < height2:
                first += 1
            else:
                last -= 1
        return max_area



