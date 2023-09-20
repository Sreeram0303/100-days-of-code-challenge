# -------------------------------------------
# problem -1 

# from typing import List
# def calculateNumberOfDays(s: str) -> int:
#     # write your code here
#     cnt = 0
#     result = 0
#     for i in range(len(s)):
#         if s[i] == '1':
#             cnt += 1
#         else:
#             result += (cnt + 1) // 2
#             cnt = 0
#     result += (cnt+1) // 2
#     return result

# -------------------------------------------
# problem -2

# from typing import List
# def sameDigits(n: int) -> int:
#     # Write your code here.
#     s = [int(x) for x in str(n)]
#     f = s[0]
#     dip = False
#     for i in range(len(s)):
#         if s[i] > f and not dip:
#             f += 1
#             break
#         elif s[i] < f:
#             dip = True
#     j = ""
#     for i in range(len(s)):
#         j += str(f)
#     return int(j)

# -------------------------------------------
# problem -3

# def multipleSum(n: int, arr: List[int]) -> int:
#     # Write your code here.
#     # sum = 0
#     # for i in range(len(arr)):
#     #     for j in range(len(arr)):
#     #         if arr[j] % arr[i] == 0:
#     #             sum += arr[j] 
#     # return sum
#     arr.sort()
#     m = arr[-1]
#     a = [0]*(m+1)
#     for i in range(n):
#         for j in range(arr[i],m+1,arr[i]):
#             a[j] += 1
#     ans = 0
#     for i in range(n):
#         ans += a[arr[i]] * arr[i]
    # return ans