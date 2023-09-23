# -----------------------------------
# problem-1

# from typing import List
# from collections import defaultdict
# def happyKids(balls : List[int]) -> int:
#     # Write your code here.
#     HM = defaultdict(int)
#     for i in balls:
#         HM[i] += 1
#     mx = -1
#     for x,y in HM.items():
#         if (y >= 2) and (x > mx):
#             mx = x
#     return mx 

# ------------------------------------
# problem-2
# ---------partially accepted--------------
# def productionHouse(n: int, m: int, days: List[int], needs: List[int]) -> int:
#     HM = defaultdict(int)
#     for i in range(len(days)):
#         HM[days[i]] = i
#     N = 0
#     for i in range(1,m+1):
#         N += n
#         if i in days:  
#             if N >= needs[HM[i]]:
#                 N -= needs[HM[i]]
#             else:
#                 return 0
#     return 1