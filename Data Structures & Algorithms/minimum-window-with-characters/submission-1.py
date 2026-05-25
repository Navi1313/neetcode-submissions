class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) :
            return ""    
        count = len(t)
        start = 0 
        end  = 0
        vals = [0]*128
        ans = float('inf')
        # update count by 1 in vals array by looking values from t 
        for i in t:
            vals[ord(i)] +=1

        while end < len(s):
            if vals[ord(s[end])] > 0:
                count -=1
            vals[ord(s[end])] -=1
            end+=1

            while count == 0:
                if ans > end-start:
                    index = start
                    ans = end-start

                if vals[ord(s[start])] == 0:
                    count +=1
                vals[ord(s[start])] +=1
                start +=1
        return "" if ans ==  float('inf') else s[index:index+ans]



            

            

