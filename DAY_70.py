# ------------------------------------

# problem-1
# Maximum area rectangle in binary matrix
# -->Break the input 2D matrix into 1D matrix
# 0 1 1 0
# 1 1 1 1
# 1 1 1 1
# 1 1 0 0
# H1-> 0 1 1 0
# add the 2nd row to the first if the adding element is 1
# H2-> 1 2 2 1
# H3-> 2 3 3 2
# H4->3 4 0 0 (the element in 4 th row is 0 so no need to add instead turn it into zero)
# -->After converting into 1D arrays apply the maximum area of histogram(MAH) method
# -->The max of all the 1D arrays MAH values will be the answer

# --------------------------------
# problem-2
from typing import List

# def getTrappedWater(arr: List[int]) -> int:
#     """
#     Calculate the amount of water trapped between the bars in the given list.

#     Args:
#     - arr: A list of integers representing the heights of the bars.

#     Returns:
#     - The total amount of water trapped between the bars.
#     """
#     if len(arr) <= 1:
#         return 0

#     n = len(arr)
#     mxl = [0] * n
#     mxr = [0] * n
#     mxl[0] = arr[0]
#     mxr[n-1] = arr[n-1]

#     for i in range(1, n):
#         mxl[i] = max(mxl[i-1], arr[i])
#         mxr[n-i-1] = max(mxr[n-i], arr[n-i-1])

#     total_water = 0
#     for i in range(n):
#         total_water += min(mxl[i], mxr[i]) - arr[i]

#     return total_water
