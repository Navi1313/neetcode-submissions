class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        start = 0
        end =  n-1
        f = -1
        l = -1
        
        while start <= end:
            mid = (start + end)//2
            if nums[mid] == target:
                f = mid
                end = mid-1
            elif nums[mid] < target : 
                start = mid+1
            else:
                end = mid-1
        start = 0 
        end = n-1        
        while start <= end:
            mid = (start + end)//2
            if nums[mid] == target:
                l = mid
                start = mid+1
            elif nums[mid] < target : 
                start = mid+1
            else:
                end = mid-1     
        return [f,l]                  


        