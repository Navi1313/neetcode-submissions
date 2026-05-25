class Solution:
    def c(self , n , memo ) -> int:
        if n==0:
            return 1
        if n<0:
            return 0

        if n in memo :
            return memo[n]
        memo[n] = self.c(n-1,memo) + self.c(n-2 ,memo)
        return memo[n]

    def climbStairs(self, n: int) -> int:
        # if n<=3:
        #     return n
        # a2=2
        # a3=3
        # for i in range(3,n):
        #     a3,a2 = a2+a3 , a3
        # return a3
        memo = {}
        return self.c(n, memo)
