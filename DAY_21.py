# ---------------------------------------------------
# problem-1
# Number of occurrences

# from collections import defaultdict
# def count(arr: [int], n: int, x: int) -> int:
# ----------------BETTER SOL
#     # Your code goes here
#     # HM = defaultdict(int)
#     # for i in arr:
#     #     HM[i]+=1
#     # for k,y in HM.items():
#     #     if k == x:
#     #         return y
#     # return 0
# --------------------BRUTE FORCE
#     # cnt = 0
#     # for i in arr:
#     #     if i == x:
#     #         cnt += 1
#     # return cnt
# --------------OPTIMAL SOLUTION
#     first = -1
#     low = 0
#     high = n-1
#     while low <= high:
#         mid = low - (low - high) // 2
#         if arr[mid] == x:
#             first = mid
#             high = mid-1
#         elif arr[mid] > x:
#             high = mid - 1
#         else:
#             low = mid + 1
#     last = -1
#     low = 0
#     high = n-1
#     while low <= high:
#         mid = low - (low - high) // 2
#         if arr[mid] == x:
#             last = mid
#             low = mid + 1
#         elif arr[mid] > x:
#             high = mid - 1
#         else:
#             low = mid + 1
#     if first == -1:
#         return 0
#     else:
#         return last - first + 1 

# -----------------------------------
# problem-2
# Search in a rotatedsortedarray with no duplicates

# def searchInARotatedSortedArrayII(arr : List[int], k : int) -> bool:
#     # Write your code here.
#     n = len(arr)
#     low = 0
#     high = n - 1
#     while low <= high:
#     	mid = low - (low - high) // 2
#     	if arr[mid] == k:
#     		return True
#     	elif arr[low] <= arr[mid]:
#     		if arr[low] <= k and k  <= arr[mid]:
#     			high = mid-1
#     		else:
#     			low = mid + 1
#     	else:
#     		if arr[mid] <= k and  k <= arr[high]:
#     			low = mid + 1
#     		else:
#     			high = mid-1
#     return False

# --------------------different model------------------

# def searchInARotatedSortedArrayII(arr : List[int], k : int) -> bool:
    # n = len(arr)  # size of the array
    # low, high = 0, n - 1

    # while low <= high:
    #     mid = (low + high) // 2

    #     # if mid points to the target
    #     if arr[mid] == k:
    #         return True

    #     # Edge case:
    #     if arr[low] == arr[mid] and arr[mid] == arr[high]:
    #         low += 1
    #         high -= 1
    #         continue

    #     # if left part is sorted
    #     if arr[low] <= arr[mid]:
    #         if arr[low] <= k <= arr[mid]:
    #             # element exists
    #             high = mid - 1
    #         else:
    #             # element does not exist
    #             low = mid + 1
    #     else:  # if right part is sorted
    #         if arr[mid] <= k <= arr[high]:
    #             # element exists
    #             low = mid + 1
    #         else:
    #             # element does not exist
    #             high = mid - 1

    # return False