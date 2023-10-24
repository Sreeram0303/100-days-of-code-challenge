# problem-1
# def firstNegative(arr, n, k) :
#     # Write your code here.
#     i = 0
#     j = 0
#     ans = []
#     l = []
#     while j < n:
#         if arr[j] < 0:
#             l.append(arr[j])
#         if j-i+1 < k:
#             j += 1
#         elif j-i+1 == k:
#             if len(l) == 0:
#                 ans.append(0)
#             else:
#                 ans.append(l[0])
#                 if arr[i] == l[0]:
#                     l.remove(l[0])
#             i += 1
#             j +=1
#     return ans

# problem-2
# Understood the concept of counting anagrams