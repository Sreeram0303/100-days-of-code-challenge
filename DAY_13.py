# ---------------------------------------------
#problem-1
#Set Matrix Zeros------
# BRUTE SOL ----- TC - nearly O(N*3)
# def markRow(matrix, n, m, i):
#     # set all non-zero elements as -1 in the row i:
#     for j in range(m):
#         if matrix[i][j] != 0:
#             matrix[i][j] = -1

# def markCol(matrix, n, m, j):
#     # set all non-zero elements as -1 in the col j:
#     for i in range(n):
#         if matrix[i][j] != 0:
#             matrix[i][j] = -1

# def zeroMatrix(matrix, n, m):
#     # Set -1 for rows and cols
#     # that contains 0. Don't mark any 0 as -1:
#     for i in range(n):
#         for j in range(m):
#             if matrix[i][j] == 0:
#                 markRow(matrix, n, m, i)
#                 markCol(matrix, n, m, j)
    
#     # Finally, mark all -1 as 0:
#     for i in range(n):
#         for j in range(m):
#             if matrix[i][j] == -1:
#                 matrix[i][j] = 0
    
#     return matrix
# ------------------BETTER SOLUTION - TC - O(2*(N*M)),,,,,SC - O(N) + O(M)
# def zeroMatrix(matrix, n, m):
#     # Write your code here.
#     row = [0]*n
#     col = [0]*m
#     for i in range(n):
#         for j in range(m):
#             if matrix[i][j] == 0:
#                 row[i] = 1
#                 col[j] = 1
#     for i in range(n):
#         for j in range(m):
#             if row[i] or col[j]:
#                 matrix[i][j] = 0
#     return matrix
# -----------------------------OPTIMAL APPROACH --/ ---------O(2X(n*m))
# def zeroMatrix(matrix, n, m):
#     # int row[n] = {0}; --> matrix[..][0]
#     # int col[m] = {0}; --> matrix[0][..] 

#     col0 = 1
#     # step 1: Traverse the matrix and
#     # mark 1st row & col accordingly:
#     for i in range(n):
#         for j in range(m):
#             if matrix[i][j] == 0:
#                 # mark i-th row:
#                 matrix[i][0] = 0

#                 # mark j-th column:
#                 if j != 0:
#                     matrix[0][j] = 0
#                 else:
#                     col0 = 0

#     # Step 2: Mark with 0 from (1,1) to (n-1, m-1):
#     for i in range(1, n):
#         for j in range(1, m):
#             if matrix[i][j] != 0:
#                 # check for col & row:
#                 if matrix[i][0] == 0 or matrix[0][j] == 0:
#                     matrix[i][j] = 0

#     #step 3: Finally mark the 1st col & then 1st row:
#     if matrix[0][0] == 0:
#         for j in range(m):
#             matrix[0][j] = 0
#     if col0 == 0:
#         for i in range(n):
#             matrix[i][0] = 0

#     return matrix

# ---------------------------------------------
#problem-2
#Rotate a matrix 90 degrees
# def rotateMatrix(mat):----------OPTIMAL solution
#     # Write your code here.
#     for i in range(len(mat)-1):
#         for j in range(i+1,len(mat[0])):
#             mat[i][j],mat[j][i] = mat[j][i],mat[i][j]
#     for i in range(len(mat)):
#         mat[i].reverse()
#     return mat

# BRUTE FORCE------------
# store the values in the new array in their correct positions--------