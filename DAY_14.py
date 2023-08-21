# --------------------------------------
#problem - 1
# def findAllSubarraysWithGivenSum(arr, s):
# #     # # Write your code here.------------BETTER SOL
# #     # cnt = 0
# #     # n = len(arr)
# #     # for i in range(n):
# #     #     sum = 0
# #     #     for j in range(i,n):
# #     #         sum += arr[j]
# #     #         if sum == s:
# #     #             cnt += 1
# #     # return cnt 
#     HM = defaultdict(int) ----------------------OPTIMAL SOL ---counted number of x-targetsum are possible 
#     HM[0] = 1--------------default dic set default value of any key is 0 unless mentioned
#     presum = 0
#     cnt = 0
#     for i in range(len(arr)):
#         presum += arr[i]
#         remove = presum - s
#         cnt += HM[remove]
#         HM[presum] += 1
#     return cnt

# ------------------------------------------------

# Problem-2
# pascal triangle
# variation - 1
# In this case, we are given the row number r and the column number c, and we need to find out the element at position (r,c). 
# import math
# def nCr(n, r):
#     ans = 1
#     for i in range(r):
#         ans = ans * (n - i)
#         ans = ans // (i + 1)

#     return ans
# def pascalTriangle(r, c):
#     element = nCr(r - 1, c - 1)
#     return element
#Variation-2
# Given the row number n. Print the n-th row of Pascal’s triangle.
# import math
# def nCr(n, r):
#     ans = 1
#     for i in range(r):
#         ans = ans * (n - i)
#         ans = ans // (i + 1)
#     return ans
# def pascalTriangle(n):
#     for c in range(1, n+1):
#         print(nCr(n-1, c-1), end=" ")
#     print()
# Variation-3
# from typing import *

# def generateRow(row):
#     ans = 1
#     ansRow = [1] #inserting the 1st element
    
#     #calculate the rest of the elements:
#     for col in range(1, row):
#         ans *= (row - col)
#         ans //= col
#         ansRow.append(ans)
#     return ansRow

# def pascalTriangle(n : int) -> List[List[int]]:
#     ans = []
    
#     #store the entire pascal's triangle:
#     for row in range(1, n+1):
#         ans.append(generateRow(row))
#     return ans