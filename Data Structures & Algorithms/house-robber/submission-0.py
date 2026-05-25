class Solution:
    def rob(self, nums: List[int]) -> int:
        def fun(i):
            if i>=len(nums):
                return 0 

            if i in memo:
                return memo[i]
            memo[i] = max(nums[i] +fun(i+2) , fun(i+1))
            return memo[i]

        memo = {}
        return fun(0)