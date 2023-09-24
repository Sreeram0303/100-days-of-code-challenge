# ------------------------------------------------
# problem-1

# def subsetSum(arr: List[int]) -> List[int]:
#         ans = []
#         def subsetSumsHelper(ind: int, sum: int):
#             if ind == len(arr):
#                 ans.append(sum)
#                 return
#             # element is picked
#             subsetSumsHelper(ind + 1, sum + arr[ind])
#             # element is not picked
#             subsetSumsHelper(ind + 1, sum)
#         subsetSumsHelper(0, 0)
#         ans.sort()
#         return ans

# ---------------------------------------------------
# problem-2

# def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
#         ans = []
#         res = set()
#         def fun(index: int, ds: List[int]):
#             if index == len(nums):
#                 ds.sort()
#                 res.add(tuple(ds))
#                 return
#             ds.append(nums[index])
#             fun(index + 1, ds)
#             ds.pop()
#             fun(index + 1, ds)
#         fun(0, [])
#         for it in res:
#             ans.append(list(it))
#         return ans