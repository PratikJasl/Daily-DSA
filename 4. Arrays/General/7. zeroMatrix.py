#Make the matrix zero
#arr = [[1,1,1],[1,0,1],[1,1,1]]

#Brute Force: T:O((m*n)*(m+n))
#Step1: Iterate through the matrix.
#Step2: When you find a zero mark it -1.
#Step3: Iterate through the matrix and mark -1 to 0.
def setZeroes(self, matrix: List[List[int]]) -> None:
    n = len(matrix) # no of columns
    m = len(matrix[0]) # no of rows

    def markRow(matrix, n, m, i):
        for j in range(m):
            if matrix[i][j] != 0:
                matrix[i][j] = -1

    def markCol(matrix, n, m, j):
        for i in range(n):
            if matrix[i][j] != 0:
                matrix[i][j] = -1

    #Call the mark row and column functions.
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                markRow(matrix, n, m, i)
                markCol(matrix, n, m, j)
    
    #Replace all -1 with 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == -1:
                matrix[i][j] = 0
    
    return matrix

        