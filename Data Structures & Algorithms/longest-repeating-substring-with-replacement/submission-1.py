class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # O(N2) APPROACH
        # maxi = 0 
        # for i in range(0 , len(s)):
        #     maxC = 0 
        #     nums = [0]*26
        #     for j in range(i, len(s)):
        #         m = s[j]
        #         nums[ ord(m) - ord('A')] +=1
        #         maxC = max(maxC ,nums[ ord(m) - ord('A')])

        #         change = (j-i+1) - maxC

        #         if change  > k:
        #             break
        #         maxi = max(maxi , j-i+1)
        # return maxi
        i = 0 
        j = 0 
        nums = [0]*26
        maxi = 0
        maxC = 0
        for j in range(len(s)):
            val = s[j]
            nums[ord(val) - ord('A')] +=1
            maxC = max(maxC ,nums[ord(val) - ord('A')])

            change = j-i+1-maxC
            if change > k:
                nums[ord(s[i])-ord('A')] -=1
                i +=1
            maxi = max(maxi , j-i+1)
        return maxi    


