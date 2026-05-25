class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #  Brute force 
        if len(s) != len(t):
            return False
        # Brute Force Approach (o(nlogn))
        # s = sorted(s)
        # t = sorted(t)
        # for i in range(len(t)):
        #     if s[i] != t[i]:
        #        return False
        # return True   

        l = [0]*128
        for i in t : 
            l[ord(i)] +=1

        for j in s:
            l[ord(j)] -=1

#  Checking any negitive count inside 
        for count in l:
            if count != 0:
                return False

        return True           








        