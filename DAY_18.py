# -----------------------------------------------
# PROBLEM - 1
# from typing import *

# -------------------OTHER APPROACH
# def numberOfInversions(a : List[int], n : int) -> int:
#     # Write your code here.
#     cnt = 0
#     for i in range(n):
#         for j in range(i+1,n):
#             if i < j and a[i] > a[j]:
#                 cnt +=1
#     return cnt    
#     while i < n:
#         j = i + 1

# ---------------------------OPTIMAL SOLN
# from typing import List
# import math
# def merge(arr : List[int], low : int, mid : int, high : int) -> int:
#     temp = []   # temporary array
#     left = low  # starting index of left half of arr
#     right = mid + 1 # starting index of right half of arr

#     cnt = 0     # Modification 1: cnt variable to count the pairs

#     # storing elements in the temporary array in a sorted manner
#     while (left <= mid and right <= high):
#         if (arr[left] <= arr[right]):
#             temp.append(arr[left])
#             left += 1
#         else:
#             temp.append(arr[right])
#             cnt += (mid - left + 1)  # Modification 2
#             right += 1

#     # if elements on the left half are still left
#     while (left <= mid):
#         temp.append(arr[left])
#         left += 1

#     # if elements on the right half are still left
#     while (right <= high):
#         temp.append(arr[right])
#         right += 1

#     # transfering all elements from temporary to arr
#     for i in range(low, high + 1):
#         arr[i] = temp[i - low]

#     return cnt   # Modification 3

# def mergeSort(arr : List[int], low : int, high : int) -> int:
#     cnt = 0
#     if low >= high:
#         return cnt
#     mid = math.floor((low + high) / 2)
#     cnt += mergeSort(arr, low, mid)    # left half
#     cnt += mergeSort(arr, mid + 1, high)  # right half
#     cnt += merge(arr, low, mid, high)  # merging sorted halves
#     return cnt

# def numberOfInversions(a : List[int], n : int) -> int:
#     # Count the number of pairs:
#     n = len(a)
#     # Count the number of pairs:
#     return mergeSort(a, 0, n - 1)

# ---------------------------------------------
# problem-2
# count inversion

# def team(skill: [int], n: int) -> int:-----------------BrUTE FORCE
#     # Write your code here.
#     cnt = 0
#     for i in range(n):
#         for j in range(i+1,n):
#             if i<j and skill[i] > skill[j]*2:
#                 cnt += 1
#     return cnt

# from typing import List---------------OPTIMAL SOLUTION (BASED ON MERGE SORT)

# def merge(arr, low, mid, high):
#     temp = []  # temporary array
#     left = low  # starting index of left half of arr
#     right = mid + 1  # starting index of right half of arr

#     # storing elements in the temporary array in a sorted manner
#     while left <= mid and right <= high:
#         if arr[left] <= arr[right]:
#             temp.append(arr[left])
#             left += 1
#         else:
#             temp.append(arr[right])
#             right += 1

#     # if elements on the left half are still left
#     while left <= mid:
#         temp.append(arr[left])
#         left += 1

#     # if elements on the right half are still left
#     while right <= high:
#         temp.append(arr[right])
#         right += 1

#     # transferring all elements from temporary to arr
#     for i in range(low, high + 1):
#         arr[i] = temp[i - low]

# def countPairs(arr, low, mid, high):
#     right = mid + 1
#     cnt = 0
#     for i in range(low, mid + 1):
#         while right <= high and arr[i] > 2 * arr[right]:
#             right += 1
#         cnt += (right - (mid + 1))
#     return cnt

# def mergeSort(arr, low, high):
#     cnt = 0
#     if low >= high:
#         return cnt
#     mid = (low + high) // 2
#     cnt += mergeSort(arr, low, mid)  # left half
#     cnt += mergeSort(arr, mid + 1, high)  # right half
#     cnt += countPairs(arr, low, mid, high)  # Modification
#     merge(arr, low, mid, high)  # merging sorted halves
#     return cnt

# def team(skill: [int], n: int) -> int:
#     return mergeSort(skill, 0, n - 1)


