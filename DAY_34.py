# ----------------------------------------------
# # problem-1

# from typing import *
# from collections import defaultdict
# class Solution:
#     def beautySum(self, s: str) -> int:
#         def beauty(s):
#             HM = defaultdict(int)
#             for i in s:
#                 if i not in HM.keys():
#                     HM[i] = 1
#                 else:
#                     HM[i] += 1
#             lst = list(HM.values())
#             return max(lst) - min(lst)

#         total_beauty = 0
#         for i in range(len(s)):
#             ans = ""
#             for j in range(i, len(s)):
#                 ans += s[j]
#                 total_beauty += beauty(ans)
#         return total_beauty

# ------------------------------------------------
# problem-2

# def reverseString(s:str) -> str:
#     # Write your code here
#     lst = s.split()
#     lst.reverse()
#     ans = " ".join(lst)
#     return ans

# def reverseWords(self, s: str) -> str:
#         ans = ""
#         temp = ""
#         i = 0
#         while i < len(s):
#             if s[i] != " ":
#                 temp += s[i]
#             elif s[i] == " " and temp != "":
#                 ans = temp + " " + ans
#                 temp = ""
#             i += 1
#         # Add the last word to the result if it's not empty
#         if temp != "":
#             ans = temp + " " + ans
#             temp = ""
#         return ans.strip()  # Remove trailing space if any

#  ------------------------------------------------
# problem-3

    # def longestPalindrome(self, s: str) -> str:
        # def isPalindrome(self, s):
    #     return s == s[::-1]
    #     temp = ""
    #     mx = 0  # Initialize mx to 0
    #     for i in range(len(s)):
    #         ans = ""
    #         for j in range(i, len(s)):
    #             ans += s[j]
    #             if self.isPalindrome(ans) and len(ans) > mx:
    #                 mx = len(ans)
    #                 temp = ans
    #     return temp
