class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Method 1 :
        # O(NLOGN ) , Space O(N)
        # lis = sorted(set(nums))
        # ans = 1
        # big_ans = 0
        # if len(lis) == 1 :
        #     return 1 

        # for i in range(1,len(lis)):
        #     if lis[i] - lis[i-1] == 1:
        #         ans +=1 
        #         big_ans = max(big_ans , ans)

        #     else:
        #        big_ans = max(big_ans , ans)
        #        ans = 1
        # return big_ans  

        # Method 2 
        numset = set(nums)
        longest = 0 

        for num in numset:
            if num-1 not in numset:
                length = 1 

                while num +length in numset:
                    length +=1
                longest = max(longest, length)
        return longest            
        
        
