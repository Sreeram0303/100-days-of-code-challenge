# --------------------------------------
# problem-1
# -------------------BRUTE FORCE--------------
# def singleNonDuplicate(arr):
    # n = len(arr)  # Size of the array
    # if n == 1:
    #     return arr[0]

    # for i in range(n):
    #     # Check for first index
    #     if i == 0:
    #         if arr[i] != arr[i + 1]:
    #             return arr[i]
    #     # Check for last index
    #     elif i == n - 1:
    #         if arr[i] != arr[i - 1]:
    #             return arr[i]
    #     else:
    #         if arr[i] != arr[i - 1] and arr[i] != arr[i + 1]:
    #             return arr[i]

    # # Dummy return statement
    # return -1
# -------------------OPTIMAL SOLUTION-------------------
# def singleNonDuplicate(arr):
#     n = len(arr)  # Size of the array

#     # Edge cases:
#     if n == 1:
#         return arr[0]
#     if arr[0] != arr[1]:
#         return arr[0]
#     if arr[n - 1] != arr[n - 2]:
#         return arr[n - 1]

#     low = 1
#     high = n - 2
#     while low <= high:
#         mid = (low + high) // 2

#         # If arr[mid] is the single element:
#         if arr[mid] != arr[mid + 1] and arr[mid] != arr[mid - 1]:
#             return arr[mid]

#         # We are in the left:
#         if (mid % 2 == 1 and arr[mid] == arr[mid - 1]) or (mid % 2 == 0 and arr[mid] == arr[mid + 1]):
#             # Eliminate the left half:
#             low = mid + 1
#         # We are in the right:
#         else:
#             # Eliminate the right half:
#             high = mid - 1

#     # Dummy return statement:
#     return -1

# --------------------------------------------
# problem-2

# def findPeakElement(arr: [int]) -> int:
#     n = len(arr)  # Size of the array

#     # Edge cases:
#     if n == 1:
#         return 0
#     if arr[0] > arr[1]:
#         return 0
#     if arr[n - 1] > arr[n - 2]:
#         return n - 1

#     low = 1
#     high = n - 2
#     while low <= high:
#         if arr[low] <= arr[low+1]:
#             low += 1
#         else:
#             return low
        

    # while low <= high:
    #     mid = (low + high) // 2

    #     # If arr[mid] is the peak:
    #     if arr[mid - 1] < arr[mid] and arr[mid] > arr[mid + 1]:
    #         return mid

    #     # If we are in the left:
    #     if arr[mid] > arr[mid - 1]:
    #         low = mid + 1

    #     # If we are in the right:
    #     # Or, arr[mid] is a common point:
    #     else:
    #         high = mid - 1

    # Dummy return statement
    # return -1