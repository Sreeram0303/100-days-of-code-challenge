# -----------------------------------------------------------#

# Problem-1
# def longestSubarrayWithSumK(a: [int], k: int) -> int:-----------------------------------TC - O(N^2)
#     # Write your code here
#     mx = 0
    
#     for i in range(len(a)):
#         j = i
#         sume = 0
#         while j<len(a) and sume <= k:
#             sume += a[j]
#             if sume == k:
#                 sz = j - i +1
#                 mx = max(sz,mx)
#             j+=1

        
#     return mx

#------------------------------------------APPROACH 2 - optimal approach----------------------
# def longestSubarrayWithSumK(a: [int], k: int) -> int:
#     mx = 0
#     i = 0
#     j = 0
#     sum = a[0]
#     mx = 0
#     while j < len(a):
#         while i<=j and sum > k:
#             sum -= a[i]
#             i += 1
#         if sum == k:
#             mx = max(mx,j-i+1)
#         j += 1
#         if j < len(a):
#             sum += a[j]
#     return mx

# -----------------------------------------------------------#

# Problem-2 https://www.geeksforgeeks.org/longest-sub-array-sum-k/ resource
# from os import *
# from sys import *
# from collections import *
# from math import *

# def getLongestSubarray(arr: [int], k: int) -> int:
 
#     # dictionary mydict implemented
#     # as hash map
#     mydict = dict()
#     n = len(arr)
#     # Initialize sum and maxLen with 0
#     sum = 0
#     maxLen = 0
 
#     # traverse the given array
#     for i in range(n):
 
#         # accumulate the sum
#         sum += arr[i]
 
#         # when subArray starts from index '0'
#         if (sum == k):
#             maxLen = i + 1
 
#         # check if 'sum-k' is present in
#         # mydict or not
#         elif (sum - k) in mydict:
#             maxLen = max(maxLen, i - mydict[sum - k])
 
#         # if sum is not present in dictionary
#         # push it in the dictionary with its index
#         if sum not in mydict:
#             mydict[sum] = i
 
#     return maxLen

# -----------------------------------------------------------#

#problem - 3
# https://www.youtube.com/watch?v=Gl-8HLvV8bc ---resource
# def traffic(n: int, m: int, vehicle: [int]) -> int:
    # Write your code here.
    # max1 = 0  -----------------------Number of continuous 1's in the array
    # cnt = 0
    # for i in range(n):
    #     if vehicle[i] == 1:
    #         cnt+=1
    #         max1 = max(cnt,max1)
    #     else:
    #         cnt = 0
    # return max1
# def traffic(n: int, m: int, vehicle: [int]) -> int:

    # i = 0 ---------------------------------Number of continue 1's after flipping m number of zeroes
    # j = 0
    # zc = 0
    # mx = 0
    # while j < n:
    #     if vehicle[j] == 0:
    #         zc += 1
    #     while zc > m:
    #         if vehicle[i] == 0:
    #             zc -= 1
    #         i += 1
    #     mx = max(mx,j-i+1)
    #     j += 1
    # return mx

# -----------------------------------------------------------#

#problem-4
#Two SUM
# def twoSum(self, nums: List[int], target: int) -> List[int]: -------------- APPROACH 1
#         HM = {}
#         for i in range(len(nums)):
#             a = nums[i]
#             more = target - a
#             if more in HM.keys():
#                 return [i,HM[more]]
#             else:
#                 HM[nums[i]] = i
        
        # for i in range(len(nums)): --------------------------APPROACH 2
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i , j]
                    
        # return [0]
# def read(n: int, book: [int], target: int) -> str:
#     # Write your code here.
#     # for i in range(n):
#     #     for j in range(1,n):
#     #         if book[i] + book[j] == target:
#     #             return "YES"
#     # return "NO"     
#     book.sort()       
#     i = 0
#     j = n-1
#     while i < j: ----------------------optimal 2 pointer approach for YES/NO model
#         sum = book[i] + book[j]
#         if sum == target:
#             return "YES"
#         elif sum > target:
#             j -= 1
#         else:
#             i +=1
#     return "NO"

# -----------------------------------------------------------#

#problem-5
#DUTCH NATIONAL FLAG ALGORITHM
# def sortArray(arr, n): --------->sorting array containing only 0,1,2's - TC - O(n),  SC - O(1)

# 	# Write your code here
# 	low = 0
# 	mid = 0
# 	high = n-1
# 	while mid <= high:
# 		if arr[mid] == 0:
# 			temp = arr[mid]
# 			arr[mid] = arr[low]
# 			arr[low] = temp
# 			low += 1 
# 			mid += 1

# 		elif arr[mid] == 1:
# 			mid += 1
# 		else:
# 			temp = arr[high]
# 			arr[high] = arr[mid]
# 			arr[mid] =temp
# 			high -= 1
