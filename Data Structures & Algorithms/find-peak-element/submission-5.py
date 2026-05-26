class Solution:
    def findPeakElement(self, arr: List[int]) -> int:
        n = len(arr)
        start = 0 
        end = n-1
        while start <=end:
            mid = (start+end)//2
            left = float('-inf') if mid-1 ==-1 else arr[mid-1]
            right = float('-inf') if mid+1 == n else arr[mid+1]
            if arr[mid] > right and  arr[mid] > left:
                return mid
            elif arr[mid] > right and arr[mid] < left:
                end = mid-1
            else:
                start = mid+1



