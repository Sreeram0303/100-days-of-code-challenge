# from os import *
# from sys import *
# from collections import *
# from math import *

# def maxOfSubarray(nums, n, k):
#     # write your code here
#     # return a list denoting the answer.
#     i = 0
#     j = 0
#     sm = []
#     mx = []
#     while j < n:
#         while len(sm) > 0 and sm[-1] < nums[j]:
#             sm.pop()
#         sm.append(nums[j])
#         if j-i+1<k:
#             j += 1
#         elif j-i+1 == k:
#             mx.append(sm[0])
#             if sm[0] == nums[i]:
#                 sm.remove(sm[0])
#             i += 1
#             j += 1
#     return mx
