# Coding ninjas Weekend content - 94

# -----------------------------
# problem-1
# def joeAndCheeseCake(n: int, m: int) -> int:
#     # Write your code here.
#     if n < m:
#         return 1
#     elif (n % m) == 0:
#         return n // m
#     else:
#         return (n // m) + 1


# -------------------------------

# problem-2
# from typing import List

# def goodPartition(n: int, v: List[int]) -> int:
#     # Write your code here.
#     v.sort()
#     mid = len(v) // 2
#     if v[mid] != v[mid-1]:
#         return 1
#     else:
#         return 0

# --------------------------------

#problem-3
# def primecheck(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             return False
#     return True

# def intreverse(N):
#     rev = ''
#     while(N >0):
#         m = N % 10
#         if m != 0:
#             rev += str(m)
#         N = N // 10
#     return primecheck(int(rev))

# def primeReversePrime(l: int, r: int) -> int:
#     # Write your code here.
#     cnt = 0
#     for i in range(l,r+1):
#         if primecheck(i) and intreverse(i):
#             cnt += 1
#             i += 2  
#     return cnt

# -----------------------------------
# problem-4

# from typing import List
# from collections import defaultdict
# def ninjaAndLessMaxElement(n: int, a: List[int]) -> List[int]:
#     # Write your code here.
#     HM = defaultdict(int)
#     arr = [0]*len(a)
#     for i in range(len(a)):
#         if HM[a[i]] == 0 and i == 0:
#             arr[i] = -1
#             HM[a[i]] = i
#         elif HM[a[i]] == 0:
#             HM[a[i]] = i
#             j = 0
#             mx = 0
#             while j < i:
#                 if a[j] < a[i]:
#                     mx = max(mx,a[j])
#                 j += 1
#             if mx == 0:
#                 arr[i] =  - 1
#             else:
#                 arr[i] = mx
#         else:
#             j = HM[a[i]]
#             HM[a[i]] = i
#             mx = 0
#             while j < i:
#                 if a[j] < a[i]:
#                     mx = max(mx,a[j])
#                 j += 1
#             if mx == 0:
#                 arr[i] = - 1
#             else:
#                 arr[i] = mx
        
#     return arr

# print(ninjaAndLessMaxElement(32,[24, 32, 30, 6, 15, 19, 12, 13, 4, 31, 18, 
#                                  13, 9, 9, 13, 5, 5, 9, 14, 6, 18, 10, 25, 21, 
#                                  31, 12, 6, 13, 14, 2, 4, 26, 41]))