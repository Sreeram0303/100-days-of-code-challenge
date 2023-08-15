# #Merge Sort Using Python
# def merge(arr, l, m, r):
#     temp = []
#     i = l
#     j = m + 1
#     while i <= m and j <= r:
#         if arr[i] < arr[j]:  # Fix: Change arr[l] to arr[i]
#             temp.append(arr[i])
#             i += 1
#         else:
#             temp.append(arr[j])
#             j += 1
#     while i <= m:
#         temp.append(arr[i])
#         i += 1
#     while j <= r:
#         temp.append(arr[j])
#         j += 1
#     for k in range(l, r + 1):
#         arr[k] = temp[k-l]  # Adjusted index for assigning back to arr !!!!VERY IMPORTANT PLACE TO PAY ATTENTION

# def ms(arr, l, r):
#     if l >= r:
#         return
#     mid = (l + r) // 2
#     ms(arr, l, mid)
#     ms(arr, mid + 1, r)
#     merge(arr, l, mid, r)

# def mergeSort(arr: [int], l: int, r: int):
#     ms(arr, l, r)

# from typing import List

# def qs(arr, l, h):
#     i = l
#     j = h
#     piv = arr[l]
#     while i < j:
#         while i <= h and arr[i] <= piv:
#             i += 1
#         while j >= l and arr[j] > piv:
#             j -= 1
#         if i < j:
#             temp = arr[i]
#             arr[i] = arr[j]
#             arr[j] = temp
#     arr[l] = arr[j]
#     arr[j] = piv
#     return j

# def quickSort(arr: List[int], startIndex: int, endIndex: int):
#     if startIndex < endIndex:
#         piv = qs(arr, startIndex, endIndex)
#         quickSort(arr, startIndex, piv - 1)
#         quickSort(arr, piv + 1, endIndex)

# def removeDuplicates(arr,n):
#     # Write your code here.
#     # return len(list(set(arr)))
#     arr1 = []
#     for i in range(n):
#         if arr[i]!=-1:
#             arr1.append(arr[i])
#             for j in range(i+1,n):
#                 if arr[i] == arr[j]:
#                     arr[j] = -1
#     return len(arr1)

# def rotateArray(arr: [], n: int) -> []:   -------->Approach 1
#     # Write your code from here.
#     temp = arr[0]
#     for i in range(1,n):
#         arr[i-1] = arr[i]
#     arr[n-1] = temp
#     return arr

# i = 0                                     --------------->Approach 2
#     for j in range(1,n):
#         if arr[i] != arr[j]:
#             arr[i+1] = arr[j]
#             i+=1
#     return i+1

#Largest element in the array
# from os import *
# from sys import *
# from collections import *
# from math import *

# def largestElement(arr: [], n: int) -> int:

#     # Write your code from here.
#     # mx = arr[0]
#     # for i in arr:
#     #     if i >= mx:
#     #         mx = i
#     # return mx
#     s_arr = sorted(arr)
#     return s_arr[len(arr)-1]

#Second largest element in the array
# def getSecondOrderElements(n: int,  a: [int]) -> [int]: ----------Approach 1 
#     # Write your code here.
#     s_arr = sorted(a)
#     if min(a) == max(a):
#         return a[0]
#     return [ s_arr[len(a)-2] , s_arr[1] ]

# def getSecondOrderElements(n: int, a: [int]) -> [int]: ----------Approach - 2
#     if len(a) < 2:
#         return []
#     first_max = second_max = float('-inf')
#     first_min = second_min = float('inf')
#     for num in a:
#         if num > first_max:
#             second_max = first_max
#             first_max = num
#         elif num > second_max and num != first_max:
#             second_max = num
#         if num < first_min:
#             second_min = first_min
#             first_min = num
#         elif num < second_min and num != first_min:
#             second_min = num
#     return [second_max, second_min]

#IF array is sorted
# def isSorted(n: int,  a: [int]) -> int:
#     # Write your code here.
   
#     for i in range(n-1):
#         if a[i] > a[i+1]:
#             return 0 
#     return 1
    
    



# #Microsoft test 
# # result = solution(A, X, Y)
# # # print("Minimum cost:", result)
# # def solution(A, X, Y):
# #       l=len(A)
# #       sums=[]
# #       for i in range(l):
# #           total_sum=0
# #           last=i+(X-1)*Y
# #           if last<=l-1:
# #               total_sum+=sum(A[i:last+1:Y])
# #               sums.append(total_sum)
# #           else:
# #               break
# #       return min(sums)
# # A = [4, 2, 5, 4,3,5,1,4,2,7]
# # X = 3
# # Y = 2
# # print(solution(A,X,Y))

# # def solution(N,A,B):
# #   d2 = dict.fromkeys(range(N), 0)
# #   count = 0
# #   arr = []
# #   for i in range(len(A)):
# #       arr.append((A[i],B[i]))
# #   while True:
# #       for i in range(len(A)):
# #           for c in arr:
# #               if i in c:
# #                   d2[i] += 1
# #       arr1 = arr
# #       for i in range(len(A)):
# #              if d2[i] <= 1:
# #                  arr = list(filter(lambda x: x[1] != i and x[0] != i, arr))
# #       if len(arr) == len(arr1) :
      
# #           return count + 1
# #           break
# #       count += 1
# # A = [0,1,2,3]
# # B = [1,2,3,0]
# # N = 4
# # print(solution(N,A,B))

# # from collections import defaultdict
# # def solution(N, A, B):
# #     linked = defaultdict(list)
# #     for i in range(len(A)):
# #         linked[A[i]].append(B[i])
# #         linked[B[i]].append(A[i])
# #     changed = True
# #     seconds = 0
# #     removing = []
# #     while changed:
# #         changed = False
# #         seconds += 1
# #         for i in list(linked.keys())[:]:
# #             if len(linked[i]) > 1:
# #                 continue
# #             if len(linked[i]) == 1:
# #                    removing.append((linked[i][0],i))
# #             del linked[i]
# #             changed = True
# #         for i,j in removing:
# #             linked[i].remove(j)
# #         removing = []
# #     return seconds - 1
# # A = [0,1,2,3]
# # B = [1,2,3,0]
# # N = 4
# # print(solution(N,A,B))
# # def solution(A, X, Y):
# #     N = len(A)
# #     min_cost = float('inf')

# #     for i in range(N - X*Y + 1):
# #         total_cost = sum(A[i:i + X*Y:Y])
# #         min_cost = min(min_cost, total_cost)

# #     return min_cost

# # # Example usage
# # A = [4, 2, 5, 4,3,5,1,4,2,7]
# # X = 3
# # Y = 2
