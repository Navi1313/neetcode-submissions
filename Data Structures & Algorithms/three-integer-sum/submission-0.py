class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i in range(0,len(nums)-2):
            # Skiping Duplicates for value of i
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i+1 
            right = len(nums)-1
            while (left < right):
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0 :
                    left +=1
                elif sum > 0 :
                    right -=1
                else:
                    ans.append([ nums[i], nums[left], nums[right]])  
                    left +=1

                    while left < right and nums[left] == nums[left-1]:
                              left +=1
        return ans                  
                    

