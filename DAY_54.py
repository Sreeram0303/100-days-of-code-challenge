# ----------------------------
# problem-1

# def solve(ind,arr,ds,ans):
#     if ind == len(arr):
#         if sum(ds) % 2 == 0:
#             ans.append(ds[:])
#         return 
#     ds.append(arr[ind])
#     solve(ind+1,arr,ds,ans)
#     ds.pop()
#     solve(ind+1,arr,ds,ans)
# def parityProblems(arr: List[int]) -> int:
#     # Write your code here.
#     ans = []
#     ds = []
#     solve(0,arr,ds,ans)
#     mx = 0
#     for i in ans:
#         mx = max(mx,len(i))
#     return mx