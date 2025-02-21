class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        
        left, right = 0, n - 1
        result = 0
        
        while left < right:
            curr_area = min(height[left], height[right]) * (right - left)
            result = max(result, curr_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return result