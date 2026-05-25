class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        max_ans = 0 
        for i in range(0,len(s)):
            count = [0]*256
            ans = 0 
            for j in range(i , len(s)):
                if count[ord(s[j])] == 1:
                    break
                count[ord(s[j])]+=1
                ans +=1
            max_ans = max(ans , max_ans)    
        return max_ans         



