class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Function telling us that minimun steps taken after start from 0 or 1 index
        def dfs(i) :
            if i >=len(cost):
                return 0
            if i in memo :
                return memo[i]    
            memo[i] =  cost[i] + min(dfs(i+1) , dfs(i+2))
            return memo[i]

        memo  = {}   
        return min(dfs(0) , dfs(1))            