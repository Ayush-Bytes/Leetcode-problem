class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        i, j = 0, len(height) - 1
        max_height = max(height)
        while i < j:
            depth = min(height[i], height[j])
            if (j-i) * max_height < max_area:
                break
            area = depth * (j-i)
            max_area = max(max_area, area)
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return max_area