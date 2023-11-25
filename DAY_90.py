# problem - 1 

# import heapq
# def KClosest(a, n, k, x):
#     # Write your code here.
#     heap = []
#     ans = []
#     if k != x:
#         for i in a:
#             heapq.heappush(heap,(-abs(x-i),-i))
#             if len(heap) > k:
#                 heapq.heappop(heap)
#         while len(heap) > 0:
#             ans.append(-(heapq.heappop(heap)[1]))
#         ans.sort()
#     return ans
