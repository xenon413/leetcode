class Solution:
    def maxArea(self, height: list[int]) -> int:
        # init
        left = 0
        right = len(height)-1
        width = len(height) - 1
        res = min(height[left], height[right])*width 
        while True:
            width -= 1
            if height[left] > height[right]:
                right -=1

            elif height[left] < height[right]:
                left += 1
            
            else: 
                left += 1
                right -= 1
                width -= 1 

            # break point
            if left >= right:
                break
            
            res = max(res, min(height[left], height[right])*width )

        return res