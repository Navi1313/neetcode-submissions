class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax = 0 
        rightmax = 0 
        left = 0 
        right = len(height)-1
        water = 0 
        while left <= right : 

            if leftmax <= rightmax : 
                if leftmax <= height[left]:
                    leftmax = height[left]
                else:    
                    water += leftmax - height[left]
                left +=1
            else:
                if rightmax <= height[right]:
                    rightmax = height[right]
                else:    
                    water +=rightmax - height[right]
                right -=1


        return water         


        