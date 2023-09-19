# ---------------------------------
# problem-1

# def myPow(x: float, n: int) -> float:
#     ans = 1.0
#     nn = n
#     if nn < 0:
#         nn = -1 * nn
#     while nn:
#         if nn % 2:
#             ans = ans * x
#             nn = nn - 1
#         else:
#             x = x * x
#             nn = nn // 2
#     if n < 0:
#         ans = 1.0 / ans
#     return ans

#
# ------------------------------------
# problem-2

# def generateString(N: int) -> List[str]:
#     # write your code here
    
#     if N == 0:
#         return [""]
#     if N == 1:
#         return ["0", "1"]
#     result = []
#     for s in generateString(N - 1):
#         result.append(s + "0")
#         if s[-1] != '1':
#             result.append(s + "1")
#     return result

#  ------------------------------------
# problem-3

# from typing import List

# def good(n,digit):
#     lst = [int(x) for x in str(n)]
#     if digit in lst:
#         return False
#     for i in range(len(lst)):
#         temp = lst[i]
#         for j in range(i+1,len(lst)):
#             if temp <= lst[j]:
#                 return False
#             temp -= lst[j]
#     return True
    
# def goodNumbers(a: int, b:int, digit:int) -> List[int]:
#     ans = []
#     for i in range(a,b+1):
#        if good(i,digit):
#            ans.append(i)
#     return ans
        