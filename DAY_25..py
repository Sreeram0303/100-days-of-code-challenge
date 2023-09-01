# -------------------------------------
# problem-1

# def check(arr,n,x):
#     sum = 0
#     for i in range(len(arr)):
#         sum += ceil(arr[i]/n)
#     if sum > x:
#         return 1
#     elif sum < x:
#         return 2
#     else:
#         return 0
# def smallestDivisor(arr: [int], limit: int) -> int:
#     # Write your code here.
#     ans = -1
#     low = 1
#     high = max(arr)
#     while low <= high:
#         mid = (low + high) // 2
#         if check(arr,mid,limit) == 0 or check(arr,mid,limit) == 2:
#             ans = mid
#             high = mid - 1
#         else: 
#             low = mid + 1
        
    
#     return ans

# -----------------------------------------
# problem-2

# def findDays(weights, cap):
#     days = 1  # First day
#     load = 0
#     n = len(weights)  # Size of array
#     for i in range(n):
#         if load + weights[i] > cap:
#             days += 1  # Move to next day
#             load = weights[i]  # Load the weight
#         else:
#             # Load the weight on the same day
#             load += weights[i]
#     return days

# def leastWeightCapacity(weights, d):
#     # Find the maximum and the summation
#     low = max(weights)
#     high = sum(weights)
#     while low <= high:
#         mid = (low + high) // 2
#         numberOfDays = findDays(weights, mid)
#         if numberOfDays <= d:
#             # Eliminate right half
#             high = mid - 1
#         else:
#             # Eliminate l
#             low = mid + 1
#     return low

# -----------------------------------
# problem-3

# from typing import *
# def missingK(vec: List[int], n: int, k: int) -> int:
    # Write your code here.
    # j = []---------------------------1 brute force
    # for i in range(1,max(vec)):
    #     if i not in vec:
    #         j.append(i)
    # return j[k-1]
                    
    # for i in range(n):-------------------2 brute force
    #     if vec[i] <= k:
    #         k += 1
    #     else:
    #         break
    # return k

    # OPTIMAL SOLUTION
    # low = 0
    # high = n - 1
    # while low <= high:
    #     mid = (low + high) // 2
    #     missing = vec[mid] - (mid + 1)
    #     if missing < k:
    #         low = mid + 1
    #     else:
    #         high = mid - 1
    # return k + high + 1