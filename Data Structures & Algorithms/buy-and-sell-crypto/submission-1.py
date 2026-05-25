class Solution:
    def maxProfit(self, arr: List[int]) -> int:
        mini = arr[0]
        ans =0
        for i in arr:
            ans = max(ans , i-mini)
            mini = min(mini , i)
        return ans
            
            