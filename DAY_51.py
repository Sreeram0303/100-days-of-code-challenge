# --------------------------------
# problem-1

# class Solution:
#     ans = []
#     ds = []
#     def recurperm(self,nums,freq):
#         if len(self.ds) == len(nums):
#             self.ans.append(self.ds.copy())
#             return
#         for i in range(len(nums)):
#             if not freq[i]:
#                 self.ds.append(nums[i])
#                 freq[i] = 1
#                 self.recurperm(nums,freq)
#                 freq[i] = 0
#                 self.ds.pop()
        
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         self.ans = []
#         self.ds = []
#         freq = [0] * len(nums)
#         self.recurperm(nums, freq)
#         return self.ans

# --------------------------------------------
# problem-2

# class Solution:
#     def solve(self,IP,OP,j):
#         if len(IP) == 0:
#             j.append(OP)
#             return
#         OP1 = OP
#         OP2 = OP
#         OP1 += " "
#         OP1 += IP[0]
#         OP2 += IP[0]
#         IP = IP[1:]
#         self.solve(IP,OP1,j)
#         self.solve(IP,OP2,j)
#     def permutation (self, S):
#         # code here
#         IP = S[1:]
#         OP = S[0]
#         j = []
#         self.solve(IP,OP,j)
#         return j

# ------------------------------------------
# problem-3

# class Solution:
#     def solve(self,IP,OP,j):
#         if len(IP) == 0:
#             j.append(OP)
#             return
#         if IP[0].isdigit():
#             OP += IP[0]
#             IP = IP[1:]
#             self.solve(IP,OP,j)
#         else:
#             OP1 = OP
#             OP2 = OP
#             OP1 += IP[0].lower()
#             OP2 += IP[0].upper()
#             IP = IP[1:]
#             self.solve(IP,OP1,j)
#             self.solve(IP,OP2,j)
#     def letterCasePermutation(self, s: str) -> List[str]:
#         IP = s
#         OP = ""
#         j = []
#         self.solve(IP,OP,j)
#         return j