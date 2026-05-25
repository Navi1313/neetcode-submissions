class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # n = len(heights)
        # nsr = [len(heights)]*n
        # nsl = [-1]*n
        # ans = 0
        # stack1 = []
        # # finding next smallest Right element's index
        # for i in range(len(heights)):
        #     while stack1 and heights[i] < heights[stack1[-1]]:
        #         nsr[stack1[-1]] = i
        #         stack1.pop()
        #     stack1.append(i)
        # stack2 = []
        # # finding next smaalest Left elements's index
        # for i in range(len(heights)-1 , -1 , -1):
        #     while stack2 and heights[i] < heights[stack2[-1]]:
        #         nsl[stack2[-1]] = i
        #         stack2.pop()
        #     stack2.append(i)
        # # Computing the ans using formula max(height*width) from nsl and nsr
        # for i in range(0, len(nsr)):
        #     height = heights[i]
        #     width = nsr[i]-nsl[i] -1
        #     ans = max(ans , height*width)
        # return ans  
    
        n = len(heights)
        ans = 0
        stack = []
        # 2. In in pass 
        for i in range(n):
            # Iterate an check the corrosponding next smallest left and next smallest right
            while stack and heights[stack[-1]] > heights[i]:
                idx = stack.pop()
                if stack : 
                    width = i - stack[-1] -1
                    height = heights[idx]
                    ans = max(ans , height*width)
                else:
                    width = i 
                    height =heights[idx]
                    ans = max(ans , height*width)
            stack.append(i)
            # Make a stack empty chcek for the left ->? 
            # the left-out indexes in stack will be present let them out same like before
        while stack :
            idx = stack.pop()
            if stack : 
                width = n-stack[-1]-1
                height = heights[idx]
                ans = max(ans ,height*width)
            else:
                width = n
                height = heights[idx]
                ans = max(ans , height*width)  
        return ans 

