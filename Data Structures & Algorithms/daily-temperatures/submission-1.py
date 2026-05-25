class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        # O(NSQUARE) + O(N) SPACE
        # lis = [0]*n

        # for i in range(0, n-1):
        #     count = 1
        #     for j in range(i+1,n):
        #         if temperatures[i] < temperatures[j]:
        #             lis[i] = count
        #             break
        #         else:
        #             count +=1
        # return lis     

        res = [0]*n
        stack =[] #pair (temp , index)
        for i , t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT,stackIdx = stack.pop()
                res[stackIdx] = i - stackIdx
            stack.append((t,i))
        return res          



        

