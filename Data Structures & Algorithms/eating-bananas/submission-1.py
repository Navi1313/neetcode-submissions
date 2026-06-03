import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        for i in range(1, max(piles)+1):
            val = 0 
            for j in piles:
                val += math.ceil(j/i)
            if val <= h:
                return i
                    


