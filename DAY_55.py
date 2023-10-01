# -----------------------------------
# problem-1

# from typing import List
# def combinationSum2(arr: List[int], n: int, target: int) -> List[List[int]]:
#     # Write your code here.
#     arr.sort()
#     ans = []
#     ds = []
#     def solve(ind,target):
#         if target == 0:
#             ans.append(ds[:])
#             return
#         for i in range(ind,len(arr)):
#             if i > ind and arr[i-1] == arr[i]:
#                 continue
#             if arr[i] > target:
#                 break
#             ds.append(arr[i])
#             solve(i+1,target-arr[i])
#             ds.pop()
#     solve(0,target)
#     return ans


# ---------------------------------------
# problem-2

# def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
#         ans = []
#         ds = []


#         def findSubsets(ind: int):
#             ans.append(ds[:])
#             for i in range(ind, len(nums)):
#                 if i != ind and nums[i] == nums[i - 1]:
#                     continue
#                 ds.append(nums[i])
#                 findSubsets(i + 1)
#                 ds.pop()
#         nums.sort()
#         findSubsets(0)
#         return ans