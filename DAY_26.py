# --------------------------------------------
# problem-1

# def canWePlace(stalls, dist, cows):
#     n = len(stalls)  # size of array
#     cntCows = 1  # no. of cows placed
#     last = stalls[0]  # position of last placed cow
#     for i in range(1, n):
#         if stalls[i] - last >= dist:
#             cntCows += 1  # place next cow
#             last = stalls[i]  # update the last location
#         if cntCows >= cows:
#             return True
#     return False
# def aggressiveCows(stalls, k):
#     n = len(stalls)  # size of array
#     stalls.sort()  # sort the stalls
#     low = 1
#     high = stalls[n - 1] - stalls[0]
#     # apply binary search
#     while low <= high:
#         mid = (low + high) // 2
#         if canWePlace(stalls, mid, k):
#             low = mid + 1
#         else:
#             high = mid - 1
#     return high

# --------------------------------------------
# problem-2
# 
# def countStudents(arr, pages):
    # n = len(arr)  # size of array
    # students = 1
    # pagesStudent = 0
    # for i in range(n):
        # if pagesStudent + arr[i] <= pages:
            # add pages to current student
            # pagesStudent += arr[i]
        # else:
            # add pages to next student
            # students += 1
            # pagesStudent = arr[i]
    # return students
# 
# def findPages(arr, n, m):
    # book allocation impossible
    # if m > n:
        # return -1
# 
    # low = max(arr)
    # high = sum(arr)
    # while low <= high:
        # mid = (low + high) // 2
        # students = countStudents(arr, mid)
        # if students > m:
            # low = mid + 1
        # else:
            # high = mid - 1
    # return low
# 


