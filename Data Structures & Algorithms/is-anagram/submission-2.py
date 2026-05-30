class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l = [0]*128
        if len(s) != len(t):
            return False 
        for i in t : 
            l[ord(i)] +=1

        for j in s:
            l[ord(j)] -=1

#  Checking any negitive count inside 
        for count in l:
            if count != 0:
                return False

        return True          