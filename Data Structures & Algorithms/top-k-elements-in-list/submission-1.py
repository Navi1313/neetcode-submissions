class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # O(NLOGN) TIME  + O(N) Space 
        # maps = {}
        # # Adding the frequency to the maps of each number in nums ->
        # for i in nums:
        #     maps[i] = maps.get(i , 0) + 1
        # #Sorting according to values in dict : 
        # # it will return the list of tuples sorted by value of dict [(2, 4) . [3,2] , [(4,1)]
        # # because for dictionary data structure 
        # # it return dorted List of (key : value) pair means tuple
        # maps_1 = sorted(maps.items() , key = lambda item : item[1] , reverse = True)
        # # Get the top k frequent 
        # ans = [] 
        # for i in range(k):
        #     ans.append(maps_1[i][0])
        # return ans     

        # METHOD 2 
        maps = {}
        for i in nums:
            maps[i] = maps.get(i , 0) + 1

        ans = []
        for j in range(k):
            max_key_value = max(maps , key=maps.get)
            ans.append(max_key_value)
            del maps[max_key_value]

        return ans     










