class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=3:
            return n
        a2=2
        a3=3
        for i in range(3,n):
            a3,a2 = a2+a3 , a3
        return a3      