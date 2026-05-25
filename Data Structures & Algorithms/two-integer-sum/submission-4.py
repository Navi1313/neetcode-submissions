class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #  Time Complexity 0(N2)
        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] == target :
        #             return [i,j]
        # return [-1,-1]         

        #  using Sorting O(NLOGN)
        A = []
        # i -> will be treated as counter and gettin incremented and num is value in nums
        for k , num in enumerate(nums):
            A.append([num , k ])
        A.sort()
        i  , j = 0 , len(nums)-1
        while(i < j):
            val = A[i][0] + A[j][0]
            if val == target:
                return [
                min(A[i][1] , A[j][1]) ,
                max(A[i][1] , A[j][1])
                ]
            elif val < target :
                i +=1
            else:
                j -=1

        
        
