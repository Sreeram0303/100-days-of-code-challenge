# ----------------------------------
# problem-1

# BRUTE FORCE APPROACH

# class Solution:
#     def isSafe1(self, row, col, board, n):
#         # check upper element
#         duprow = row
#         dupcol = col


#         while row >= 0 and col >= 0:
#             if board[row][col] == 'Q':
#                 return False
#             row -= 1
#             col -= 1


#         col = dupcol
#         row = duprow
#         while col >= 0:
#             if board[row][col] == 'Q':
#                 return False
#             col -= 1


#         row = duprow
#         col = dupcol
#         while row < n and col >= 0:
#             if board[row][col] == 'Q':
#                 return False
#             row += 1
#             col -= 1


#         return True


#     def solve(self, col, board, ans, n):
#         if col == n:
#             ans.append(list(board))
#             return


#         for row in range(n):
#             if self.isSafe1(row, col, board, n):
#                 board[row] = board[row][:col] + 'Q' + board[row][col+1:]
#                 self.solve(col+1, board, ans, n)
#                 board[row] = board[row][:col] + '.' + board[row][col+1:]


#     def solveNQueens(self, n):
#         ans = []
#         board = ['.'*n for _ in range(n)]
#         self.solve(0, board, ans, n)
#         return ans

# OPTIMAL SOLUTION

# class Solution:
#     def solve(self, col, board, ans, leftrow, upperDiagonal, lowerDiagonal, n):
#         if col == n:
#             ans.append(board[:])
#             return


#         for row in range(n):
#             if leftrow[row] == 0 and lowerDiagonal[row+col] == 0 and upperDiagonal[n-1+col-row] == 0:
#                 board[row] = board[row][:col] + 'Q' + board[row][col+1:]
#                 leftrow[row] = 1
#                 lowerDiagonal[row+col] = 1
#                 upperDiagonal[n-1+col-row] = 1
#                 self.solve(col+1, board, ans, leftrow,
#                            upperDiagonal, lowerDiagonal, n)
#                 board[row] = board[row][:col] + '.' + board[row][col+1:]
#                 leftrow[row] = 0
#                 lowerDiagonal[row+col] = 0
#                 upperDiagonal[n-1+col-row] = 0


#     def solveNQueens(self, n: int) -> List[List[str]]:
#         ans = []
#         board = ['.'*n for _ in range(n)]
#         leftrow = [0]*n
#         upperDiagonal = [0]*(2*n-1)
#         lowerDiagonal = [0]*(2*n-1)
#         self.solve(0, board, ans, leftrow, upperDiagonal, lowerDiagonal, n)
#         return ans