class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        start = 0 
        end = n-1
        while start <= end:
            mid = (start + end) //2
            # first check in 2 sorted arrays or atleast one sorted array 
            if nums[mid] == target :
                return mid
            if nums[mid] >= nums[start]:
                # you came inside the sorted left portion
                if target <= nums[mid] and target >=nums[start]:
                    end = mid-1
                else:
                    start = mid+1
            else:
                # came to right sorted portion
                if target <= nums[end] and target >= nums[mid]:
                    start = mid+1
                else:
                    end = mid-1
        return -1                
