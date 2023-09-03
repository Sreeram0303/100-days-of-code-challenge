# --------------------------------------------
# problem-1

# def countStudents(arr, pages):
#     n = len(arr)  # size of array
#     students = 1
#     pagesStudent = 0
#     for i in range(n):
#         if pagesStudent + arr[i] <= pages:
#             # add pages to current student
#             pagesStudent += arr[i]
#         else:
#             # add pages to next student
#             students += 1
#             pagesStudent = arr[i]
#     return students

# def findPages(arr, n, m):
#     # book allocation impossible
#     if m > n:
#         return -1

#     low = max(arr)
#     high = sum(arr)
#     while low <= high:
#         mid = (low + high) // 2
#         students = countStudents(arr, mid)
#         if students > m:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return low
# def largestSubarraySumMinimized(a: [int], k: int) -> int:
#     return findPages(a,len(a),k)

# ----------------------------------------------------
# problem-2

# def countStudents(arr, pages):
#     n = len(arr)  # size of array
#     students = 1
#     pagesStudent = 0
#     for i in range(n):
#         if pagesStudent + arr[i] <= pages:
#             # add pages to current student
#             pagesStudent += arr[i]
#         else:
#             # add pages to next student
#             students += 1
#             pagesStudent = arr[i]
#     return students

# def findPages(arr, n, m):
#     # book allocation impossible
#     if m > n:
#         return -1

#     low = max(arr)
#     high = sum(arr)
#     while low <= high:
#         mid = (low + high) // 2
#         students = countStudents(arr, mid)
#         if students > m:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return low
# def findLargestMinDistance(a:list, k:int):
#     # Write your code here
#     # Return an integer
#     return findPages(a,len(a),k)

# same as book allocation problem which i did yesterday but different problem statements
