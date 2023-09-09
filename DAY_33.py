# --------------------------------------------------
# problem-1

# from collections import defaultdict
# def sortByFrequency(n: int, s: str) -> str:
#     # Write your code here

#     ans = ""
#     HM = defaultdict(int)
#     for i in s:
#         if i not in s:
#             HM[i] = 1
#         else:
#             HM[i] += 1
    
#     HM = dict(sorted(HM.items(),key = lambda x:x[1],reverse = True))
#     for x,y in HM.items():
#         i = 0 
#         while i < y:
#             ans += x
#             i += 1
#     return ans 

# --------------------------------------------
# problem-2

# def maxDepth(self, s: str) -> int:
#          depth = 0
#          cnt = 0
#          for i in s:
#              if i == '(':
#                  cnt += 1
#              elif i == ')':
#                  cnt -= 1
#              depth = max(depth,cnt)
#          return depth

# --------------------------------------------------
# problem-3
# class Solution:
#     def romanToInt(self, s: str) -> int:
    
#         def value(r):
#     	    if (r == 'I'):
#     	    	return 1
#     	    if (r == 'V'):
#     	    	return 5
#     	    if (r == 'X'):
#     	    	return 10
#     	    if (r == 'L'):
#     	    	return 50
#     	    if (r == 'C'):
#     	    	return 100
#     	    if (r == 'D'):
#     	    	return 500
#     	    if (r == 'M'):
#     	    	return 1000
#     	    return -1
#         res = 0
#         i = 0
#         while (i < len(s)):
#         	# Getting value of symbol s[i]
#         	s1 = value(s[i])
#         	if (i + 1 < len(s)):
#         		# Getting value of symbol s[i + 1]
#         		s2 = value(s[i + 1])
#         		# Comparing both values
#         		if (s1 >= s2):
#         			res = res + s1
#         			i = i + 1
#         		else:
#         			res = res + s2 - s1
#         			i = i + 2
#         	else:
#         		res = res + s1
#         		i = i + 1
#         return res

# --------------------------------------------
# problem-4

# from typing import *
# def countSubStrings(s: str, k: int) -> int:
#     hash = [0] * 26
#     ans = 0
#     for i in range(len(s)):
#         count = 0
#         hash = [0] * 26
#         for j in range(i, len(s)):
#             index = ord(s[j]) - ord('a')
#             if hash[index] == 0:
#                 count += 1
#             hash[index] += 1
#             if count == k:
#                 ans += 1
#             elif count > k:
#                 break
    # return ans

