# problem -1 

# from typing import List
# import heapq
# def KMostFrequent(n: int, k: int, arr: List[int]) -> List[int]:
#     # write your code here
#     HM = {}
#     for i in arr:
#         if i not in HM:
#             HM[i] = 1
#         else:
#             HM[i]+=1
#     heap = []
#     for i in HM.keys():
#         heapq.heappush(heap,(HM[i],i))
#         if len(heap) > k:
#             heapq.heappop(heap)
#     ans = []
#     while len(heap):
#         ans.append(heapq.heappop(heap)[1])
#     return ans

# problem - 2
# def frequencySort(self,arr):
#         HM = {}
#         for i in arr:
#             if i not in HM:
#                 HM[i] = 1
#             else:
#                 HM[i]+=1
#         heap = []
#         for i in HM.keys():
#             heapq.heappush(heap,(HM[i],-i))
#         ans = []
#         while len(heap)>0:
#             j = heapq.heappop(heap)
#             i = 0
#             while i != j[0]:
#                 ans.append(-j[1])
#                 i += 1
#         print(ans)
#         return ans