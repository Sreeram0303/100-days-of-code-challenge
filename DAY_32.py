# -----------------------------------
# problem-1

# 1st variation
# from typing import List
# def commonPrefix(arr: List[str], n: int) -> str:
#     # Write your code here
#     ans = ""
#     arr.sort()
#     first = arr[0]
#     last = arr[-1]
#     for i in range(min(len(first),len(last))):
#         if first[i] != last[i] and ans != "":
#             return ans
#         elif first[i] != last[i]:
#             return -1
#         ans += first[i]
#     if ans == "":
#         return -1
#     else:
#         return ans
# 2nd variation
# def longestCommonPrefix(self, strs: List[str]) -> str:
#         strs.sort()
#         first = strs[0]
#         last = strs[-1]
#         ans = ""
#         for i in range(min(len(first),len(last))):
#             if first[i] != last[i]:
#                 return ans
#             ans += first[i]
#         return ans

# -----------------------------------
# problem-2

#  def isIsomorphic(self, str1: str, str2: str) -> bool:
#         map1 = []
        # map2 = []
        # for idx in s:
        #     map1.append(s.index(idx))
        # for idx in t:
        #     map2.append(t.index(idx))
        # if map1 == map2:
        #     return True
        # print(map1)
        # print(map2)
        # return False

# -----------------------------------
# problem-3

# def rotateString(self, A: str, B: str) -> bool:
#         if  A == B :
#             return True
#         q1, q2 = deque(A), deque(B)
#         i = 0
#         while i < len(A) :
#             q1.append(q1.popleft())
#             if q1 == q2 :
#                 return True
#             i += 1
#         # return False 
# # ---------------------ONE LINER--------------
# def rotateString(self, s: str, goal: str) -> bool:
#     return len(s) == len(goal) and s in goal+goal 

# -----------------------------------
# problem-4

# def isAnagram(self, str1: str, str2: str) -> bool:
#         if len(str1) != len(str2):
#             return False
#         S1 = sorted(str1)
#         S2 = sorted(str2)
#         return S1 == S2