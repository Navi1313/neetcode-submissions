class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Approach 1 
        # map = {}
        # for i in range(len(nums)):

        #     map[nums[i]] = map.get(nums[i] , 0) +1

        # for i in range(len(map)):
        #     if map[nums[i]] >1:
        #        return True   

        # return False      

        # Approach 2 
        # seen = set()
        # for i in nums:
        #     if i in seen:
        #         return True
        #     seen.add(i)     
        # return False    

        # Approach 3 
        seen = set()
        for i in nums:
            seen.add(i)
        return True if len(seen) != len(nums) else False    

