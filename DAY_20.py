# --------------------------------------
# problem -1 
# Binary Search
# def bs(nums,low,high,target):--------------recurssion
#     if low > high:
#         return -1
#     mid = (low + high) // 2
#     if nums[mid] == target:
#         return mid
#     elif nums[mid] > target:
#         return bs(nums,low,mid-1,target)
#     else:
#         return bs(nums,mid+1,high,target)
# def search(nums: [int], target: int):-------Iterative
#     # write your code logic !!
#     low = 0
#     high = len(nums)-1
#     while low <= high:
#         mid = low - (low - high)//2
#         if nums[mid] == target:
#             return mid
#         elif nums[mid] > target:
#             high = mid-1
#         else:
#             low = mid + 1
#     return -1
    # return bs(nums,0,len(nums)-1,target)

# --------------------------------------------------
# Problem-2
# Lower Bound
# def lowerBound(arr: [int], n: int, x: int) -> int:
#     Write your code here------------------Brute force 
#     i = n - 1
#     res = float("inf")
#     while i >= 0:
#         if arr[i] >= x:
#             res = min(res,i)
#         i -= 1
#     if res == float("inf"):
#         return n
#     return res
# ---------------------------Optimal sol
#     low = 0
#     high = n-1
#     ans = n
#     while low <= high:
#         mid = low - (low-high)//2
#         if arr[mid] >= x:
#             ans = mid
#             high = mid - 1
#         else:
#             low = mid + 1
#     return ans
# ----------------------------------------------
# problem - 3
# Inserting in the the sorted array----------same as lower bound
# def searchInsert(arr: [int], n: int) -> int:
#     # Write your code here.
#     low = 0
#     high = len(arr)-1
#     ans = len(arr)
#     while low <= high:
#         mid = low - (low-high)//2
#         if arr[mid] >= n:
#             ans = mid
#             high = mid - 1
#         else:
#             low = mid + 1
#     return ans

# ----------------------------------------------
# problem - 4

# def upperBound(arr: [int], n: int, x: int) -> int:
#  low = 0
#     high = n-1
#     ans = n
#     while low <= high:
#         mid = low - (low-high)//2
#         if arr[mid] > x:
#             ans = mid
#             high = mid - 1
#         else:
#             low = mid + 1
#     return ans
# -------------------------------------------------------------------
#problem-5
#  def findFloor(arr, n, x):
#         low = 0
#         high = n - 1
#         ans = -1
#         while low <= high:
#             mid = (low + high) // 2
#             # maybe an answer
#             if arr[mid] <= x:
#                 ans = arr[mid]
#                 # look for smaller index on the left
#                 low = mid + 1
#             else:
#                 high = mid - 1  # look on the right
#         return ans
#     def findCeil(arr, n, x):
#         low = 0
#         high = n - 1
#         ans = -1
    
#         while low <= high:
#             mid = (low + high) // 2
#             # maybe an answer
#             if arr[mid] >= x:
#                 ans = arr[mid]
#                 # look for smaller index on the left
#                 high = mid - 1
#             else:
#                 low = mid + 1  # look on the right
    
#         return ans

#  -------------------------------------------------------------------
#problem-6

# def lowerBound(arr: [int], n: int, x: int) -> int:
#     low = 0
#     high = n-1
#     ans = n
#     while low <= high:
#         mid = low - (low-high)//2
#         if arr[mid] >= x:
#             ans = mid
#             high = mid - 1
#         else:
#             low = mid + 1
#     return ans
# def upperBound(arr: [int], n: int, x: int) -> int:
#     low = 0
#     high = n-1
#     ans = n
#     while low <= high:
#         mid = low - (low-high)//2
#         if arr[mid] > x:
#             ans = mid
#             high = mid - 1
#         else:
#             low = mid + 1
#     return ans
# def firstAndLastPosition(arr, n, k):
#     lb = lowerBound(arr,n,k)
#     ub = upperBound(arr,n,k)
#     if lb == n or arr[lb]!=k:
#         return -1,-1
#     else:
#         return lb,ub-1
# ----------------------BRUTE FORCE
#     # Write your code here
#     # first = inf
#     # last = -1
#     # for i in range(n):
#     #     if arr[i] == k:
#     #         first = min(first,i)
#     #         last = max(last,i)
#     # if last == -1:
#     #     first = -1
#     # return first,last
