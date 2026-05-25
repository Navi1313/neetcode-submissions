class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        maps = {}
        # Adding the frequency to the maps of each number in nums ->
        for i in nums:
            maps[i] = maps.get(i , 0) + 1
        #Sorting according to values in dict : 
        maps_1 = sorted(maps.items() , key = lambda item : item[1] , reverse = True)
        # Get the top k frequent 
        ans = [] 
        for i in range(k):
            ans.append(maps_1[i][0])
        return ans     
