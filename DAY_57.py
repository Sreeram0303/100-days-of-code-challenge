# -----------------------------
# problem-1

# from typing import List
# def sudokuSolver(board: List[List[int]]) -> bool:
#     # Write your code here
#     def isposs(board,row,col,d):
#         for i in range(9):
#             if board[i][col] == d:
#                 return False
#             if board[row][i] == d:
#                 return False
#             if board[3*(row // 3)+(i // 3)][3*(col//3)+(i // 3)] == d:
#                 return False
#         return True
#     for i in range(len(board)):
#         for j in range(len(board[0])):
#             if board[i][j] == 0:
#                 for d in [1,2,3,4,5,6,7,8,9]:
#                     if isposs(board,i,j,d):
#                         board[i][j] = d
#                         if sudokuSolver(board):
#                             return True
#                         else:
#                             board[i][j] = 0
#                 return False
#     return True

