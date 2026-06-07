class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # brute Force : O(M*N)
        n = len(matrix)
        for i in range(0 ,n):
            for j in range(0,len(matrix[0])):
                if matrix[i][j] == target :
                    return True
        return False            
