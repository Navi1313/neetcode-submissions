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
        div = 1
        count0 = 0 
        for i in range(len(nums)):
            if nums[i] == 0 :
                count0 +=1
                continue
            else:
                div *= nums[i]  

        if count0 >1:
            return [0 for i in range(len(nums))]
        L = []    
        for i in range(len(nums)):
            if count0 == 1 and nums[i] == 0:
                L.append(div)
            elif count0 == 1 and nums[i] !=0:
                L.append(0)     
            else:
                L.append(div//nums[i])

        return L        






        