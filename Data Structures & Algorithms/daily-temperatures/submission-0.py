class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        lis = [0]*n

        for i in range(0, n-1):
            count = 1
            for j in range(i+1,n):
                if temperatures[i] < temperatures[j]:
                    lis[i] = count
                    break
                else:
                    count +=1
        return lis       