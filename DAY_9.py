# --------------------------------------------------------------------#

# PROBLEM - 1
#Rotate array K times left --------------------APPROACH - 1
# n = int(input()) 
# arr=input().split()
# arr = [int(x) for x in arr]
# k = int(input())
# k = k % n --------------To reduce the number of times the array need to shifted if greater than n cz after every n rotations the array will be equal
# for i in range(k):
#     temp = arr[0]
#     for j in range(1,n):
#         arr[j-1] = arr[j]
#     arr[n-1] = temp
# for i in arr:
#     print(i,end=' ')
# --------------APPROACH - 2
# temp = [arr[x] for x in range(k)]
# for i in range(k,n):
#     arr[i-k] = arr[i]
# for i in range(n-k,n):
#     arr[i] = temp[i-(n-k)]
# for i in arr:
#     print(i,end=' ')

# -----------------------------------------------------------------#

#Problem - 2
# Move Zeroes to right end
# def moveZeros(n: int,  a: [int]) -> [int]:---------APPROACH 1
    # Write your code here.
    # j = []
    # for i in range(n):
    #     if a[i]  != 0:
    #         j.append(a[i])
    # if len(a) != len(j):
    #     for i in range(len(a) - len(j)):
    #         j.append(0)
    # return j
    #-------------------------APPROACH - 1
    # j = -1
    # for i in range(n):
    #     if a[i] == 0:
    #         j = i
    #         break
    # if j == -1:
    #     return a
    # for i in range(j+1,n):
    #     if a[i] != 0:
    #         temp = a[i]
    #         a[i] = a[j]
    #         a[j] = temp
    #         j += 1
    # return a

# -----------------------------------------------#

# problem - 3 an easy one
# def linearSearch(n: int, num: int, arr: [int]) -> int:
#     # Write your code here.
#     for x in range(n):
#         if arr[x] == num:
#             return x
#     return -1

# -----------------------------------------------#

# Problem - 4
#find the missing number
# def missingNumber(self, nums: List[int]) -> int:
#     if(len(nums)==0):
#         return 0
#     nums.sort()
#     for i in range(len(nums)):
#         if(i!=nums[i]):
#             return i
#     return len(nums) 

# -----------------------------------------------#

# Problem - 5 counting max number of consecutive 1's
# n = 3 
# m = 1
# vehicle = [0, 1, 1]
# def traffic(n: int, m: int, vehicle: [int]) -> int:
#     # Write your code here.
#     max1 = 0
#     cnt = 0
#     for i in range(n):
#         if vehicle[i] == 1:
#             cnt+=1
#             max1 = max(cnt,max1)
#         else:
#             cnt = 0
#     return max1
# print(traffic(n,m,vehicle))

# -----------------------------------------------#

#problem - 6
#Number that appeared only once 

# from typing import *
# def getSingleElement(arr : List[int]) -> int: --------With O(logn) - TC
#     # Write your code here.
#     HM = {}
#     for i in range(len(arr)):
#         if arr[i] in HM:
#             HM[arr[i]] += 1
#         else:
#             HM[arr[i]] = 1
        
        
#     for x,y in HM.items():
#         if y == 1:
#             return x

# ---------------------Approach - 1-----------------------# O(n) -- TC

# def getSingleElement(arr: List[int]) -> int:
#     result = 0
#     for num in arr:
#         result ^= num
#     return result

# -----------------------------------------------#
