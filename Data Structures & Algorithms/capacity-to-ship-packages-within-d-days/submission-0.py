class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n = len(weights)
        start = max(weights)
        end = sum(weights)
        while start <= end :
            mid = (start + end)//2
            count = 1
            we = 0
            for i in range(n):
                we +=weights[i]
                if we > mid:
                    count +=1
                    we = weights[i]
            if count <= days:
                ans = mid
                end = mid-1
            else:
                start = mid+1           
        return ans       