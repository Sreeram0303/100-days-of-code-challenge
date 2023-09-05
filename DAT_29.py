# -------------------------------------------
# problem-1


# def median(matrix: [[int]], m: int, n: int) -> int:
#     # Write your code here.
#     def count(row,mid):
#         l = 0
#         h = len(row)-1
#         while l<=h:
#             m = (l+h)//2
#             if row[m] <= mid:
#                 l = m + 1
#             else:
#                 h = m - 1
#         return l
#     low = 1
#     high = 10**9
#     while low <= high:
#         mid = (low+high)//2
#         cnt = 0
#         for i in range(m):
#             cnt += count(matrix[i],mid)
#         if cnt <= (n*m)//2:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return low


# -------------------------------------------
# problem-2


# -------------------BRUTE FORCE SOLN--------------
# def minimiseMaxDistance(arr, k):
#     n = len(arr)  # size of array
#     howMany = [0] * (n - 1)

#     # Pick and place k gas stations:
#     for gasStations in range(1, k + 1):
#         # Find the maximum section and insert the gas station:
#         maxSection = -1
#         maxInd = -1
#         for i in range(n - 1):
#             diff = arr[i + 1] - arr[i]
#             sectionLength = diff / (howMany[i] + 1)
#             if sectionLength > maxSection:
#                 maxSection = sectionLength
#                 maxInd = i
#         # insert the current gas station:
#         howMany[maxInd] += 1

#     # Find the maximum distance i.e. the answer:
#     maxAns = -1
#     for i in range(n - 1):
#         diff = arr[i + 1] - arr[i]
#         sectionLength = diff / (howMany[i] + 1)
#         maxAns = max(maxAns, sectionLength)
#     return maxAns

# ------------------- BETTER SOLN--------------using priority queues
# def minimiseMaxDistance(arr, k):
#     n = len(arr)  # size of array.
#     howMany = [0] * (n - 1)
#     pq = []
#     # insert the first n-1 elements into pq
#     # with respective distance values:
#     for i in range(n - 1):
#         heapq.heappush(pq, ((-1)*(arr[i + 1] - arr[i]), i))
#     # Pick and place k gas stations:
#     for gasStations in range(1, k + 1):
#         # Find the maximum section
#         # and insert the gas station:
#         tp = heapq.heappop(pq)
#         secInd = tp[1]

#         # insert the current gas station:
#         howMany[secInd] += 1

#         inidiff = arr[secInd + 1] - arr[secInd]
#         newSecLen = inidiff / (howMany[secInd] + 1)
#         heapq.heappush(pq, (newSecLen*(-1), secInd))
#     return pq[0][0]*(-1)


# --------------------------------------------
# PROBLEM-3


# -------------------------FIRST THOUGHT IN MY MIND (BRUTE FORCE)
# def median(a: int, b: int) -> float:
#     # Write the function here.
#     j = []
#     low = 0
#     high = 0
#     while low < len(a) and high < len(b):
#         if a[low] <= b[high]:
#             j.append(a[low])
#             low += 1
#         else:
#             j.append(b[high])
#             high+=1
#     while low < len(a):
#         j.append(a[low])
#         low += 1
#     while high < len(b):
#         j.append(b[high])
#         high += 1
#     # print(j)
#     # print(j[(len(j)-1)//2])
#     if len(j) % 2 == 0:
#         return (j[(len(j)-1)//2] + j[(len(j)-1)//2 + 1]) / 2
#     else:
#         return float(j[(len(j)-1)//2])

# ------------------------OPTIMAL SOLUTION---------------------------
# def median(a, b):
#     n1, n2 = len(a), len(b)
#     # if n1 is bigger swap the arrays:
#     if n1 > n2:
#         return median(b, a)

#     n = n1 + n2  # total length
#     left = (n1 + n2 + 1) // 2  # length of left half
#     # apply binary search:
#     low, high = 0, n1
#     while low <= high:
#         mid1 = (low + high) // 2
#         mid2 = left - mid1
#         # calculate l1, l2, r1, and r2;
#         l1, l2, r1, r2 = float('-inf'), float('-inf'), float('inf'), float('inf')
#         if mid1 < n1:
#             r1 = a[mid1]
#         if mid2 < n2:
#             r2 = b[mid2]
#         if mid1 - 1 >= 0:
#             l1 = a[mid1 - 1]
#         if mid2 - 1 >= 0:
#             l2 = b[mid2 - 1]

#         if l1 <= r2 and l2 <= r1:
#             if n % 2 == 1:
#                 return float(max(l1, l2))
#             else:
#                 return (float(max(l1, l2)) + float(min(r1, r2))) / 2.0

#         # eliminate the halves:
#         elif l1 > r2:
#             high = mid1 - 1
#         else:
#             low = mid1 + 1
#     return 0  # dummy statement

# -----------------------------------
# problem-4

# --------------------------BRUTE FORCE SOLUTION----------------------
# def kthElement(a: [int], n: int, b: [int], m: int, k: int) -> int:
#     j = []
#     low = 0
#     high = 0
#     while low < len(a) and high < len(b):
#         if a[low] <= b[high]:
#             j.append(a[low])
#             low += 1
#         else:
#             j.append(b[high])
#             high+=1
#     while low < len(a):
#         j.append(a[low])
#         low += 1
#     while high < len(b):
#         j.append(b[high])
#         high += 1
#     # print(j)
#     # print(j[(len(j)-1)//2])
#     return j[k-1]
# --------------------------OPTIMAL SOLUTION--------------------
# def kthElement(array1: [int], m: int, array2: [int], n: int, k: int) -> int:
#     # Write your code from here.
#     p1 = 0
#     p2 = 0
#     counter = 0
#     answer = 0


#     while (p1 < m and p2 < n):
#         if (counter == k):
#             break
#         elif (array1[p1] < array2[p2]):
#             answer = array1[p1]
#             p1 += 1
#         else:
#             answer = array2[p2]
#             p2 += 1
#         counter += 1
#     if (counter != k):
#         if (p1 != m-1):
#             answer = array1[k-counter]
#         else:
#             answer = array2[k-counter]
#     return answer
