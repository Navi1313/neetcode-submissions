class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Method 1 :
        # O(N * N) Time and Space O(N)
        # ans = []
        # for i in range(len(nums)):
        #     sum = 1 
        #     for j in range(len(nums)):
        #         if i !=j :
        #             sum *= nums[j]
        #     ans.append(sum)
        # return ans   

        # Method 2 :  
        # Using Division Operator  /
        # O(N) tIME and O(N)  Space :
        # div = 1
        # count0 = 0 
        # for i in range(len(nums)):
        #     if nums[i] == 0 :
        #         count0 +=1
        #         continue
        #     else:
        #         div *= nums[i]  

        # if count0 >1:
        #     return [0 for i in range(len(nums))]
        # L = []    
        # for i in range(len(nums)):
        #     if count0 == 1 and nums[i] == 0:
        #         L.append(div)
        #     elif count0 == 1 and nums[i] !=0:
        #         L.append(0)     
        #     else:
        #         L.append(div//nums[i])

        # return L        

        # Method 3 : Without division operator 
        # Prefix and suffix sum : 
        
        # n= len(nums)
        # res = [1]*n
        # prefix= [1]*n
        # suffix = [1]*n
        # for i in range(1,n):
        #     prefix[i] = nums[i-1] * prefix[i-1]

        # for j in range(n-2 , -1 , -1):
        #     suffix[j] = nums[j+1] * suffix[j+1]

        # for k in range(n):
        #     res[k] = prefix[k] * suffix[k]

        # return res          

        # METHOD 3 : BY NOT TAKING PREFIX AND POS FIX 
        n = len(nums)
        res = [1]*n
        prefix = 1 
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(n-1, -1,-1):
            res[i] *=postfix
            postfix *=nums[i]

        return res         
        






        