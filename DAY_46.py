# ----------------------------------------
# problem-1

# def solve(i, s, f, j):
#     if i == len(s):
#         j.append("".join(f))  # Convert the list of characters to a string and append it to the result list
#         return
    
#     # picking
#     f.append(s[i])
#     solve(i + 1, s, f, j)
    
#     # popping out while backtracking
#     f.pop()
#     solve(i + 1, s, f, j)

# def generateSubsequences(s: str) -> List[str]:
#     j = []
#     solve(0, s, [], j)  # Pass an empty list as 'f' to start with an empty subsequence
#     return j

# ----------------------------------------
# problem-2

# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         ans = []
#         ds = []


#         def findCombination(ind: int, target: int):
#             if ind == len(candidates):
#                 if target == 0:
#                     ans.append(ds[:])
#                 return
#             if candidates[ind] <= target:
#                 ds.append(candidates[ind])
#                 findCombination(ind, target - candidates[ind])
#                 ds.pop()
#             findCombination(ind + 1, target)
#         findCombination(0, target)
#         return ans


# ----------------------------------------
# problem-3

# from typing import List
# def combinationSum2(candidates: List[int],n, target: int) -> List[List[int]]:-------------------takes more time 
#     ans = set()
#     ds = []

#     candidates.sort()
    
#     def findCombination(ind: int, target: int):
#         if ind == len(candidates):
#             if target == 0:
#                 ans.add(tuple(ds[:]))  # Use tuple to store combinations in the set
#             return
#         if candidates[ind] <= target:
#             ds.append(candidates[ind])
#             findCombination(ind + 1, target - candidates[ind])
#             ds.pop()
#         findCombination(ind + 1, target)

#     findCombination(0, target)
    
#     # Convert the set of tuples back to a list of lists
#     result = [list(comb) for comb in ans]
#     result.sort()
#     return result

