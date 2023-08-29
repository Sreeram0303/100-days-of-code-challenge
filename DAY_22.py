# --------------------------------------
# problem-1

# def findMin(arr: [int]):
    # low = 0
    # high = len(arr) - 1
    # ans = sys.maxsize

    # while low <= high:
    #     mid = (low + high) // 2

    #     # search space is already sorted
    #     # then arr[low] will always be
    #     # the minimum in that search space:
    #     if arr[low] <= arr[high]:
    #         ans = min(ans, arr[low])
    #         break
            
    #     if arr[low] <= arr[mid]:  # if left part is sorted
    #         ans = min(ans, arr[low])  # keep the minimum
    #         low = mid + 1  # eliminate left half

    #     else:  # if right part is sorted
    #         ans = min(ans, arr[mid])  # keep the minimum
    #         high = mid - 1  # eliminate right half

    # return ans

# --------------------------------------
# problem-2
# def findKRotation(arr : [int]) -> int:
#     # Write your code here.
    
#     low = 0
#     high = len(arr) - 1
#     ans = float('inf')
#     index = -1
#     while low <= high:
#         mid = (low + high) // 2

#         # If search space is already sorted,
#         # then arr[low] will always be
#         # the minimum in that search space
#         if arr[low] <= arr[high]:
#             if arr[low] < ans:
#                 index = low
#                 ans = arr[low]
#             break

#         # If left part is sorted
#         if arr[low] <= arr[mid]:
#             # Keep the minimum
#             if arr[low] < ans:
#                 index = low
#                 ans = arr[low]

#             # Eliminate left half
#             low = mid + 1
#         else:  # If right part is sorted
#             # Keep the minimum
#             if arr[mid] < ans:
#                 index = mid
#                 ans = arr[mid]

#             # Eliminate right half
#             high = mid - 1

#     return index
