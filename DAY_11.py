# ----------------------------------------------#

# PROBLEM-1

# def majorityElement(v: [int]) -> int: -----------------Better Approach used Hashing----TC- O(nlogn)
#     HM = {}
#     for i in range(len(v)):
#         if v[i] in HM:
#             HM[v[i]] += 1
#         else:
#             HM[v[i]] = 1
#     for x,y in HM.items():
#         if y >= (len(v) /2):
#             return x

# def majorityElement(v: [int]) -> int: ----------------------Optimal Approach - # Moore voting Algotithm
    # ele = v[0]
    # cnt = 0
    # for i in range(len(v)):
    #     if cnt == 0:
    #         ele = v[i]
    #         cnt = 1
    #     elif ele == v[i]:
    #         cnt += 1
    #     else:

    #         cnt -= 1
    # for i in v:
    #     if ele == i:
    #         return ele

# ----------------------------------------------#

#PROBLEM-2
#KADANES ALGORITHM
# def maxSubarraySum(arr, n) : -------------------oPTMAL SOLUTION 

# def maxSubArray(self, nums: List[int]) -> int:
#         flag = 0
#         sum = 0
#         for i in nums: ------------------TO CHECK WHETHER THE ELEMENTS ARE ONLY NEGATIVE OR BOTH POSITIVE AND NEGATIVE
#             if i > 0:
#                 flag = 1
#         if flag == 0: --------------------------IF ALL THE ELEMENTS ARE NEGAIVE JUST FIND THE MAXIMUM ELEMENT IN THE ARRAY
#             maxs = -inf
#             for i in range(len(nums)):
#                 if nums[i] > maxs:
#                     maxs = nums[i]
#             return maxs
#         else:
            # maxs = nums[0] ---------------------------IF THE THERE ARE BOTH POSITIVE AND NEGATIVE ELEMENTS THEN APPLY KADANES ALGO
            # for i in range(len(nums)):
            #     if sum == 0: -------------------------------TO STORE AND PRINT THE SUB ARRAY
            #           start = i
            #     sum += nums[i]
            #     if sum < 0:
            #         sum = 0
            #     elif sum > maxs:
            #         maxs = sum
            #         startind = start
            #         endind = i
            # print(nums[startind:endind+1])
            # return maxs

# ----------------------------------------------#

#PROBLEM-3

# def bestTimeToBuyAndSellStock(prices: [int]) -> int:
    # Write your code here.
    # mx = 0
    # for i in range(len(prices)): -----------------------------brute force 
    #     for j in range(i+1,len(prices)):
    #         if prices[i] < prices[j]:
    #             mx = max(mx,prices[j] - prices[i])                
    # return mx
    #  ----------------------------Optimal approach
    # mini = prices[0]
    # profit = 0
    # for i in range(1,len(prices)):
    #     cost = prices[i] - mini
    #     profit = max(cost,profit)
    #     mini = min(mini,prices[i])
    # return profit

# ----------------------------------------------#

#PROBLEM-4

# def alternateNumbers(a : List[int]) -> List[int]:
    # # Write your code here.
    # arr1 = []
    # arr2 = []
    # for i in range(len(a)):
    #     if a[i] < 0:
    #         arr1.append(a[i])
    #     else:
    #         arr2.append(a[i])
    # j = 0
    # k = 0
    # for i in range(len(a)):
    #     if i % 2 == 0:
    #         a[i] = arr2[j]
    #         j+=1
    #     else:
    #         a[i] = arr1[k]
    #         k+=1
    # return a
    # -----------------Approach - 2 TC- O(n)
    # ans = [0]*len(a)
    # pos = 0
    # neg = 1
    # for i in range(len(a)):
    #     if a[i] > 0:
    #         ans[pos] = a[i]
    #         pos += 2
    #     elif a[i] < 0:
    #         ans[neg] = a[i]
    #         neg += 2
    # return ans

# ----------------------------------------------#

#PROBLEM-5
#Next Permutation
# OPTIMAL SOLUTION
# step - 1 : Find the longest common prefix and find the break poiint
# step - 2:  Find the element > than the element at the break point but the smallest among the ConnectionResetError
# step - 3:  Try to place the remaining in ascending order
# from typing import *

# def nextGreaterPermutation(A : List[int]) -> List[int]:
#     # Write your code here.
#     ind = -1
#     for i in range(len(A)-2,-1,-1):--------step-1
#         if A[i] < A[i+1]:
#             ind = i
#             break
#     if ind == -1:  ------------if there is no next permutation then return the first permutaion
#         A.reverse()
#         return A
#     for i in range(len(A)-1,ind,-1):----------step-2
#         if A[i] > A[ind]:
#             temp = A[i]
#             A[i] = A[ind]
#             A[ind] = temp
#             break
#     A[ind+1:] = A[(len(A)-1):ind:-1] ------------step-3
#     return A
