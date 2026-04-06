class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(heights) -1

        while left < right:
            print("Area btw = ", heights[left], heights[right])
            area = (right-left) * min(heights[left], heights[right])
            if area > max_area:
                max_area = area
                print(max_area)
            if heights[left] < heights[right]:
                left +=1
            else:
                right -=1

        return max_area
        