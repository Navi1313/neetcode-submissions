class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # 3rd Solution : O(N) TIME AND O(N) SPACE (2 -Pass)
        # dic = {}
        # for i , num in enumerate(nums):
        #     dic[num] = i

        # for i , num in enumerate(nums):
        #     diff = target - num
        #     if diff in dic and i != dic[diff]:
        #         return [i , dic[diff]]
        # return []      
        
        # 4th Solution : O(N) TIME AND 0(N) SPACE   (1 -Pass)
        dic = {}
        for i , num in enumerate(nums):
            diff = target - num
            if diff in dic and i != dic[diff]:
                return [dic[diff],i]
            dic[num] = i