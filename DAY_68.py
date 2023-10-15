# problem-1

# from typing import List

# def minimumCost(n: int, x: int, y: int, s: str) -> int:
#     # Write your code here.
#     vowels = 'aeiou'
#     consonents = 'bcdfghjklmnpqrstvwxyz'
#     v = 0
#     c = 0
    
#     for i in s:
#         if i in vowels:
#             v += 1
#         else:
#             c += 1
#     return min(v*x,c*y)

# problem-2
# from typing import List

# def makeBothEqual(n: int, m: int, s: str, t: str) -> int:
#     # Write your code here.
#     if t in s:
#         return 1
#     else:
#         return 0

#problem-3

#need to be optimized 
#  from typing import List

# def maximumLength(n: int, arr: List[int]) -> int:
#     def check(a):
#         i = 0
#         j = 1
#         while i+2 < len(a) and j+2 < len(a):
#             if a[i] > a[i+2] or a[j] < a[j+2]:
#                 return False
#             i += 2
#             j += 2
#         return True

#     def generate(index, current_subsequence):
#         if index == n:
#             if check(current_subsequence):
#                 subsequences.append(current_subsequence[:])
#             return

#         # Include the current element in the subsequence
#         current_subsequence.append(arr[index])
#         generate(index + 1, current_subsequence)

#         # Exclude the current element from the subsequence
#         current_subsequence.pop()
#         generate(index + 1, current_subsequence)

#     subsequences = []
#     generate(0, [])
#     mx = 0
#     for i in range(len(subsequences)):
#         mx = max(mx,len(subsequences[i]))
#     return mx


# print(maximumLength(6,[9, 1, 5, 3, 2, 1]))