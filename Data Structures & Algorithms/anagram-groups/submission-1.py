class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #  O(N*NLOGM)
        # defaultdict(list) 
        # if in a dictionary key dosen't exists it automatically create the 
        # empty list 

        #  Initializing the default dict with elements list : 
        # res = defaultdict(list)  
        # Looping and sorting the elemts and placing to the right position 
        # for s in strs:
            # sorting the string 
            # sortedS = ''.join(sorted(s))
            # storing the same strings to corrosponding same string
            # res[sortedS].append(s)

        # return list(res.values())

        res = {}
        for s in strs:
            sortedS = ''.join(sorted(s))
            if sortedS not in res :
                res[sortedS] = []
            res[sortedS].append(s)
        return list(res.values())        


        # res = {}
        # for i in strs:
        #     count = [0]*26
        #     for c in  i:
        #         count[ord(c) -ord('a')] +=1
        #     if (tuple(count)) not in res: 
        #         res[tuple(count)] = []
        #     res[(tuple(count))].append(i)

        # return list(res.values())        



