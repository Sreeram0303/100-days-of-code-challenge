# problem - 1 
# import heapq
# def KClosestPoints(points, k):
#     # Write your code here.
#     heap = []
#     for i in range(len(points)):
#         heapq.heappush(heap,(-(points[i][0]**2 + points[i][1]**2),(points[i][0],points[i][1])))
#         if len(heap) > k:
#             heapq.heappop(heap)
#     ans = []
#     while(len(heap)):
#         ans.append(heapq.heappop(heap)[1])
#     ans.sort()
#     final_ans = []
#     for i in range(len(ans)):
#         final_ans.append(ans[i][0])
#         final_ans.append(ans[i][1])
#     return list(final_ans)

# problem - 2
# import heapq
# def connectRopes( arr, n) :

# 	# Your code goes here
# 	heap = []
# 	for i in arr:
# 		heapq.heappush(heap,i)
# 	cst = 0
# 	while len(heap)>=2:
# 		j = (heapq.heappop(heap) + heapq.heappop(heap))
# 		heapq.heappush(heap,j)
# 		cst += j
# 	return cst