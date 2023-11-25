# problem - 1

# import heapq
# def nearlySorted(arr, k):
#     # Write your code here
#     heap = []
#     ans = []
#     for num in arr:
#         heapq.heappush(heap,num)
#         if len(heap) > k:
#             ele = heapq.heappop(heap)
#             ans.append(ele)
#     for i in range(k):
#         ele = heapq.heappop(heap)
#         ans.append(ele)
#     return ans