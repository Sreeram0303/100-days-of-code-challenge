# --------------------------------------------
# problem-1
# Next Greater Element-1

# from typing import List
# def nextGreaterElement(arr: List[int], n: int) -> List[int]:
#     # Write your code here.
#     s = []
#     v = []
#     for i in range(len(arr)-1,-1,-1):
#         if len(s) == 0:
#             v.append(-1)
#         elif s[-1] > arr[i]:
#             v.append(s[-1])
#         elif s[-1] <= arr[i]:
#             while len(s) > 0 and s[-1] <= arr[i]:
#                 s.pop()
#             if len(s) == 0:
#                 v.append(-1)
#             else:
#                 v.append(s[-1])
#         s.append(arr[i])
#     v.reverse()
#     return v

# --------------------------------------------
# problem-2
# Next Greater Element-2

# def nextGreaterElement(arr: List[int], n: int) -> List[int]:
#     # Write your code here.
#     s = []
#     v = []
#     for i in range(len(arr)):
#         if len(s) == 0:
#             v.append(-1)
#         elif s[-1] > arr[i]:
#             v.append(s[-1])
#         elif s[-1] <= arr[i]:
#             while len(s) > 0 and s[-1] <= arr[i]:
#                 s.pop()
#             if len(s) == 0:
#                 v.append(-1)
#             else:
#                 v.append(s[-1])
#         s.append(arr[i])
#     return v

# --------------------------------------
# problem-3
# Next Smaller Element

# from typing import List
# def nextSmallerElement(arr: List[int], n: int) -> List[int]:
#     # Write your code here.
#     s = []
#     v = []
#     for i in range(len(arr)-1,-1,-1):
#         if len(s) == 0:
#             v.append(-1)
#         elif s[-1] < arr[i]:
#             v.append(s[-1])
#         elif s[-1] >= arr[i]:
#             while len(s) > 0 and s[-1] >= arr[i]:
#                 s.pop()
#             if len(s) == 0:
#                 v.append(-1)
#             else:
#                 v.append(s[-1])
#         s.append(arr[i])
#     v.reverse()
#     return v
