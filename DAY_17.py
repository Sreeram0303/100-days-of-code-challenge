# -------------------------------------------------

#problem-1
#Merigin sorted arrays with constant space complexity
# from typing import *
# def mergeTwoSortedArraysWithoutExtraSpace(a : List[int], b : List[int]) -> int:
    # Write your code here.
    # n = len(a)
    # m = len(b)-----------------------BRUTE FORCE
    # i = n-1
    # j = 0
    # temp = []
   
    # while i < n and j < m:
    #     if a[i] <= b[j]:
    #         temp.append(a[i])
    #         i+=1
    #     if a[i] > b[j]:
    #         temp.append(b[j])
    #         j+=1
    # while i<n:
    #     temp.append(a[i])
    #     i+=1
    # while j < m:
    #     temp.append(b[j])
    #     j+=1
    # for i in range(m+n):
    #     if i < n:
    #         a[i] = temp[i]
    #     else:
    #         b[i-n] = temp[i]
    # ------------------------OPTIMAL SOLN
    # while i >= 0 and j < m:
    #     if a[i] > b[j]:
    #         a[i] , b[j] = b[j] , a[i]
    #         i -= 1
    #         j += 1
    #     else:
    #         break
    # a.sort()
    # b.sort()

# -------------------------------------------------

#problem-2
# from typing import List

# def findMissingRepeatingNumbers(a: [int]) -> [int]:---------------OPTIMAL SOLN MATH
#     n = len(a)  # size of the array

#     # Find Sn and S2n:
#     SN = (n * (n + 1)) // 2
#     S2N = (n * (n + 1) * (2 * n + 1)) // 6

#     # Calculate S and S2:
#     S, S2 = 0, 0
#     for i in range(n):
#         S += a[i]
#         S2 += a[i] * a[i]

#     # S-Sn = X-Y:
#     val1 = S - SN

#     # S2-S2n = X^2-Y^2:
#     val2 = S2 - S2N

#     # Find X+Y = (X^2-Y^2)/(X-Y):
#     val2 = val2 // val1

#     # Find X and Y: X = ((X+Y)+(X-Y))/2 and Y = X-(X-Y),
#     # Here, X-Y = val1 and X+Y = val2:
#     x = (val1 + val2) // 2
#     y = x - val1

#     return [x, y]
# --------------------APPROACH 2
    # Write your code here
    # HM = {}
    # for i in range(len(a)):
    #     if a[i] in HM:
    #         HM[a[i]] += 1
    #     else:
    #         HM[a[i]] = 1
    # # print(HM)
    # for x,y in HM.items():
    #     if y == 2:
    #         P = x
    # Q = None
    # for i in range(1,len(a)+1):
    #     if i not in a:
    #         Q = i
    # return [P,Q]
# -----------------------APPROACH 3
    # a.sort()
    # preel = a[0]
    # for i in range(1,len(a)):
    #     if a[i] == a[i-1]:
    #         P = a[i]
    #         break
    #     preel = a[i]
    # for i in range(1,len(a)+1):
    #     if i not in a:
    #         Q = i
    # return [P,Q]
# --------------------------APPROACH 4
    # HM = [0]*(len(a)+1)
    # P = None
    # Q = None
    # for i in range(0,len(a)):
    #     HM[a[i]] += 1
    # for i in range(1,len(a)+1):
    #     if HM[i] == 2:
    #         P = i
    #     elif HM[i] == 0:
    #         Q = i
    #     if P != None and Q != None:
    #         break
    # return [P,Q]

