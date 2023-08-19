# ------------------------------------------#
# PROBLEM-1

# from typing import *
# def superiorElements(a : List[int]) -> List[int]:
#     # Write your code here.------------------APPROACH-1----O(n*2)
#     # ans = []
#     # for i in range(len(a)-1):
#     #     flag = 0    
#     #     for j in range(i+1,len(a)):
#     #         if a[i] < a[j]:
#     #             flag = 1
#     #             break
#     #     if flag == 0:
#     #         ans.append(a[i])
#     # ans.append(a[len(a)-1])
#     # ans = list(set(ans))
#     # ans.sort()
#     # return ans
# -------------------------------APPROACH - 2 ------OPTIMAL SOL ---------TC - O(N
#     ans = []
#     mx = float('-inf')
#     for i in range(len(a)-1,-1,-1):
#         if a[i] > mx:
#             ans.append(a[i])
#         mx = max(mx,a[i])
#     ans.sort()
#     return ans

# ------------------------------------------#

# PROBLEM-2
# def linearSearch(a, num):----------------------BRUTE FORCE APPROACH -- TC - O(N2)
#     n = len(a)  # size of array
#     for i in range(n):
#         if a[i] == num:
#             return True
#     return False
# def longestSuccessiveElements(a):
#     n = len(a)  # size of array
#     longest = 1
#     # pick an element and search for its consecutive numbers
#     for i in range(n):
#         x = a[i]
#         cnt = 1
#         # search for consecutive numbers using linear search
#         while linearSearch(a, x + 1):
#             x += 1
#             cnt += 1

#         longest = max(longest, cnt)
#     return longest
# ------------------------Better Approach -------- TC- O(NlogN) + O(N)
# def longestSuccessiveElements(a):
#     n = len(a)
#     if n == 0:
#         return 0

#     # sort the array
#     a.sort()
#     lastSmaller = float('-inf')
#     cnt = 0
#     longest = 1

#     # find longest sequence
#     for i in range(n):
#         if a[i] - 1 == lastSmaller:
#             # a[i] is the next element of the
#             # current sequence
#             cnt += 1
#             lastSmaller = a[i]
#         elif a[i] != lastSmaller:
#             cnt = 1
#             lastSmaller = a[i]
#         longest = max(longest, cnt)
#     return longest
# ---------------------OPTIMAL APPROACH---------O(N) + O(2*N) ~ O(3*N)
# def longestSuccessiveElements(a):
#     n = len(a)
#     if n == 0:
#         return 0
#     longest = 1
#     st = set()
#     # put all the array elements into set
#     for i in range(n):
#         st.add(a[i])

#     # Find the longest sequence
#     for it in st:
#         # if 'it' is a starting number
#         if it - 1 not in st:
#             # find consecutive numbers
#             cnt = 1
#             x = it
#             while x + 1 in st:
#                 x += 1
#                 cnt += 1
#             longest = max(longest, cnt)
#     return longest
# -----------------------MY APPROACH ----------------------O(n log n)
# from typing import *
# def longestSuccessiveElements(a : List[int]) -> int:
#     # Write your code here.
#     le = 1
#     a = list(set(a))
#     a.sort()
#     mx = 0
#     if len(a) == 0:
        #   return 0
#     for i in range(len(a)-1):
#         if a[i+1] - a[i] == 1:
#             le += 1
#             mx = max(le,mx)
#         else:
#             le = 1
#     return mx
