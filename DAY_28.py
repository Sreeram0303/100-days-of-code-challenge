# -------------------------------------------
# problem-1

# def rowWithMax1s(matrix, n, m):
#     def lowerBound(arr, n, x):
#         low = 0
#         high = n - 1
#         ans = n

#         while low <= high:
#             mid = (low + high) // 2
#             # maybe an answer
#             if arr[mid] >= x:
#                 ans = mid
#                 # look for smaller index on the left
#                 high = mid - 1
#             else:
#                 low = mid + 1  # look on the right
#         return ans
#     cnt_max = 0
#     index = -1

#     # traverse the rows:
#     for i in range(n):
#         # get the number of 1's:
#         cnt_ones = m - lowerBound(matrix[i], m, 1)
#         if cnt_ones > cnt_max:
#             cnt_max = cnt_ones
#             index = i
#     return index

# ------------------------------
# problem-2

# def searchMatrix(mat: [[int]], target: int) -> bool:
#     # Write your code here.
#     n = len(mat)
#     m = len(mat[0])
#     low = 0
#     high = (n*m)-1
#     while low<=high:
#         mid = (low + high) // 2
#         row = mid // m 
#         col = mid % m 
#         if mat[row][col] == target:
#             return True
#         elif mat[row][col] < target:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return False

# --------------------------------------------
# problem-3
# def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    # n = len(matrix)
    # m = len(matrix[0])
    # row = 0
    # col = m - 1
    # Traverse the matrix from (0, m-1):
    # while row < n and col >= 0:
        # if matrix[row][col] == target:
            # return True
        # elif matrix[row][col] < target:
            # row += 1
        # else:
            # col -= 1
    # return False
    # 