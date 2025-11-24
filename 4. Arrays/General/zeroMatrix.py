#Make the matrix zero 
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])

        def markRow(matrix, n, m, i):
            for j in range(m):
                if matrix[i][j] != 0:
                    matrix[i][j] = -1

        def markCol(matrix, n, m, j):
            # set all non-zero elements as -1 in the col j:
            for i in range(n):
                if matrix[i][j] != 0:
                    matrix[i][j] = -1

        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    markRow(matrix, n, m, i)
                    markCol(matrix, n, m, j)
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == -1:
                    matrix[i][j] = 0
        
        return matrix

        