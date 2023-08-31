# -----------------------------------------
# problem - 1

# def floorSqrt(n):
#    # write your code logic here .
#    low = 1
#    high = n
#    while low <= high:
#       mid =( low + high) // 2
#       if mid**2 <= n:
#          low = mid + 1
#       else:
#          high = mid - 1
#    return high

# -----------------------------------------
# problem - 2

# def NthRoot(n: int, m: int) -> int:
#     # Write Your Code Here
#     low = 1
#     high = m
#     while low <= high:
#         mid = (low + high) // 2
#         if mid**n == m:
#            return mid
#         elif mid**n < m:
#             low = mid + 1
            
#         else:
#             high = mid - 1
#     return -1
# -----------------------optimal solution
# def func(mid, n, m):
#     ans = 1
#     for i in range(1, n + 1):
#         ans *= mid
#         if ans > m:
#             return 2
#     if ans == m:
#         return 1
#     return 0

# def NthRoot(n: int, m: int) -> int:
#     low = 1
#     high = m
#     while low <= high:
#         mid = (low + high) // 2
#         midN = func(mid, n, m)
#         if midN == 1:
#             return mid
#         elif midN == 0:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return -1

# -------------------------------
# problem-3
# import math
# def calculateTotalHours(v, hourly):
#     totalH = 0
#     n = len(v)
#     # Find total hours
#     for i in range(n):
#         totalH += math.ceil(v[i] / hourly)
#     return totalH

# def minimumRateToEatBananas(v, h):
#     low = 1
#     high = max(v)

#     # Apply binary search
#     while low <= high:
#         mid = (low + high) // 2
#         totalH = calculateTotalHours(v, mid)
#         if totalH <= h:
#             high = mid - 1
#         else:
#             low = mid + 1
#     return low

# -------------------------------------
# problem-4

# def possible(arr, day, m, k):
#     n = len(arr)  # size of the array
#     cnt = 0
#     noOfB = 0
#     # count the number of bouquets
#     for i in range(n):
#         if arr[i] <= day:
#             cnt += 1
#         else:
#             noOfB += cnt // k
#             cnt = 0
#     noOfB += cnt // k
#     return noOfB >= m

# def roseGarden(arr, k, m):
#     val = m * k
#     n = len(arr)  # size of the array
#     if val > n:
#         return -1  # impossible case
#     # apply binary search
#     low = min(arr)
#     high = max(arr)
#     while low <= high:
#         mid = (low + high) // 2
#         if possible(arr, mid, m, k):
#             high = mid - 1
#         else:
#             low = mid + 1
#     return low


