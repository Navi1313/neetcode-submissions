class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0 
        end = len(heights)-1
        height = 0 
        while start < end:
            length = end-start
            height = max(height , length*(min(heights[start], heights[end])))
            if heights[start] >= heights[end]:
                end -=1
            else:
                start +=1
        return height            



