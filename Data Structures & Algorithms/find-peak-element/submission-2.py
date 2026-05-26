class Solution:
    def findPeakElement(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0
        if n ==2 :
            if arr[0] > arr[1]:
                return 0
            else :
                return 1  
        start = 0 
        end = n-1
        while start <=end:
            mid = start + (end-start)//2
            if mid+1 ==n or mid-1 == -1:
                val1 = float('inf')
                val2 = float('inf')
                if arr[mid] > val2 or  arr[mid] > val1:
                    return mid

            if arr[mid] > arr[mid+1] and  arr[mid] > arr[mid-1]:
                return mid
            elif arr[mid] > arr[mid+1] and arr[mid] < arr[mid-1]:
                end = mid-1
            else:
                start = mid+1


