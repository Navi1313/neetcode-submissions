class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lis = sorted(set(nums))
        ans = 1 
        big_ans = 0
        if len(lis) == 1 :
            return 1 

        for i in range(1,len(lis)):
            if lis[i] - lis[i-1] == 1:
                ans +=1 
                big_ans = max(big_ans , ans)

            else:
               big_ans = max(big_ans , ans)
               ans = 1
        return big_ans            