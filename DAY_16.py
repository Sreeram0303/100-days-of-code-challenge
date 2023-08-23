# -------------------------------------------------
#problem-1
#Longest subarray with sum 0

# from typing import *
# from collections import defaultdict
# def getLongestZeroSumSubarrayLength(arr : List[int]) -> int:----------------Better soln
#     Write your code here
#     n = len(arr)
#     le = 0
#     for i in range(n):
#         sum = 0
#         for j in range(i,n):
#             sum += arr[j]
#             if sum == 0:
#                 le = max(le,j-i+1)
#     return le            
#     n = len(arr)-----------------------------optimal soln
#     sum = 0
#     mx = 0
#     HM = defaultdict(int)
#     for i in range(n):
#         sum += arr[i]
#         if sum == 0:
#             mx= i+1
#         else:
#             if sum in HM:
#                 mx = max(mx,i - HM[sum])
#             else:
#                 HM[sum] = i
#     return mx

# -------------------------------------------------

#problem-2
# Subarrays with XOR ‘K’

# from collections import defaultdict
# def subarraysWithSumK(a: [int], b: int) -> int:
#     # Write your code here
#     n = len(a)---------------- BETTER SOLN
#     cnt = 0
#     for i in range(n):
#         sum = 0
#         for j in range(i,n):
#             sum ^= a[j]
#             if sum == b:
#                 cnt += 1
#     return cnt
#     XR = 0---------------OPTIMAL SOLN
#     HM = defaultdict(int)
#     cnt = 0
#     HM[0] = 1
#     for i in range(n):
#         XR ^= a[i]
#         x = XR ^ b
#         cnt += HM[x]
#         HM[XR] += 1
#     return cnt

# -------------------------------------------------

#problem-3
# from typing import *

# def mergeOverlappingIntervals(arr : List[List[int]]) -> List[List[int]]:
    # Write your code here.
# -----------------------BRUTE FORCE
    # ans = []
    # arr.sort()
    # for i in range(len(arr)):
    #     start,end = arr[i][0] , arr[i][1]
    #     if ans and ans[-1][1] >= end:
    #         continue
    #     for j in range(i+1,len(arr)):
    #         if arr[j][0] <= end:
    #             end = max(end,arr[j][1])
    #         else:
    #             break
    #     ans.append([start,end])
    # return ans
# -------------------------------OPTIMAL SOLN
    # ans = []
    # arr.sort()
    # for i in range(len(arr)):
    #     if not ans or arr[i][0] > ans[-1][1]:
    #         ans.append(arr[i])
    #     else:
    #         ans[-1][1] = max(ans[-1][1],arr[i][1])
    # return ans






    


