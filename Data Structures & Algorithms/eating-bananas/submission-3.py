import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Brute Force 
        # n = len(piles)
        # for i in range(1, max(piles)+1):
        #     val = 0 
        #     for j in piles:
        #         val += math.ceil(j/i)
        #     if val <= h:
        #         return i
        start = 1 
        ans = -1
        end = max(piles)+1
        while start <= end:
            mid = (start + end )// 2 
            val = 0 
            for pi in piles:
                val += math.ceil(pi/mid)
            if val <= h :
                ans = mid
                end = mid-1
            else:
                start = mid +1   
        return ans




