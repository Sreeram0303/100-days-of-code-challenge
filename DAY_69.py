# --------------------------
# problem-1
# stock span

# from typing import List
# def findStockSpans(prices: List[int]) -> List[int]:
#     v= []
#     s = []
#     for i in range(len(prices)):
#         if len(s) == 0:
#             v.append(-1)
#         elif s[-1][0] >= prices[i]:
#             v.append(s[-1][1])
#         elif s[-1][0] <= prices[i]:
#             while len(s) > 0 and s[-1][0] < prices[i]:
#                 s.pop()
#             if len(s) == 0:
#                 v.append(-1)
#             else:
#                 v.append(s[-1][1])
#         s.append((prices[i],i))
#     for i in range(len(v)):
#         v[i] = i - v[i]
#     return v

#-------------------------------
# problem-2
# Area of histogram
# ---->Find NSL 
# ---->Find NSR
# ---->store NSR-NSL-1 in width array
# ---->multiply given array with width array and store the values in new array named area
# ---->get the max of it