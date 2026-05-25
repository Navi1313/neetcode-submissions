class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxi = 0 
        for i in range(0 , len(s)):
            maxC = 0 
            nums = [0]*26
            for j in range(i, len(s)):
                m = s[j]
                nums[ ord(m) - ord('A')] +=1
                maxC = max(maxC ,nums[ ord(m) - ord('A')])

                change = (j-i+1) - maxC

                if change  > k:
                    break
                maxi = max(maxi , j-i+1)
        return maxi    