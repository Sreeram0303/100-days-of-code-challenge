# problem-1
# from typing import List
# import heapq
# def kthSmallest(n: int, j: int, arr: List[int]) -> int:
#     # write your code here
#     heap = []  
#     for num in arr:  
#         heapq.heappush(heap, num)  
      
#     kth_smallest = None  
#     for _ in range(j):  
#         kth_smallest = heapq.heappop(heap)  
      
#     return kth_smallest  

#Problem-2

# import heapq
# def kthLargest(arr, size, k):
#     # write your code here
#     heap = []  
#     for num in arr:  
#         heapq.heappush(heap, -num)  
      
#     kth_largest = None  
#     for _ in range(k):  
#         kth_largest = heapq.heappop(heap)  
      
#     return -kth_largest


