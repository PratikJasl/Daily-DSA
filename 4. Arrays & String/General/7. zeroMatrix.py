#Make the matrix zero
arr = [[1,1,1],[1,0,1],[1,1,1]]

#Brute Force: T:O((m*n)*(m+n))
#Step1: Iterate through the matrix.
#Step2: When you find a zero mark it -1.
#Step3: Iterate through the matrix and mark -1 to 0.
def setZeroes(matrix) -> None:
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

#Better Approach: T: O(M*n) S: O(m+n)
#Step1: We maintain a row and column array.
#Step2: Iterate through the loop and when we find a zero mark row and column array 1.
#Step3: Iterate through the loop and mark the indexes 0 where row and column is 1.
def setZeroesBetter(matrix):
    m = len(matrix) #rows
    n = len(matrix[0]) #columns

    row = [0] * m
    column = [0] * n

    for i in range(m):
        for j in range(n):
            if(matrix[i][j] == 0):
                row[i] = 1
                column[j] = 1
    
    for i in range(m):
        for j in range(n):
            if row[i] == 1 or column[j] == 1:
                matrix[i][j] = 0
    print("Matrix with Zero:", matrix)
    return matrix

setZeroesBetter(arr)