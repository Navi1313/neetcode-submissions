class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # brute Force : O(M*N)
        # n = len(matrix)
        # for i in range(0 ,n):
        #     for j in range(0,len(matrix[0])):
        #         if matrix[i][j] == target :
        #             return True
        # return False  

        #  2nd Approach : O(M*LOGN)
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            start = 0 
            end = m-1
            while start <= end:
                mid = (start + end )//2
                if target == matrix[i][mid]:
                    return True
                elif target < matrix[i][mid]:
                    end = mid -1
                else:
                    start = end + 1 
        return False                   
