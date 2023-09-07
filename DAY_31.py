# -------------------------------------------
# problem-1

# def maxDepth(s:str) -> int:
#     # Write your code here.
#     depth = 0
#     cnt = 0
#     for i in s:
#         if i == '(':
#             cnt += 1
#         elif i == ')':
#             cnt -= 1
#         depth = max(depth,cnt)
#     return depth

# -------------------------------------------
# problem-2

# def removeOuterParentheses(self, s: str) -> str:
#         ans = ""
#         stc = []
#         for i in s:
#             if i == "(":
#                 if len(stc) > 0:
#                     ans += "("
#                 stc.append('(')
#             elif i == ")":
#                 stc.pop()
#                 if len(stc) > 0:
#                     ans += ")"
#         return ans

# ------------------------------------------
# problem-3

# def reverseString(s: str) -> str:
#     ans = ""
#     temp = ""
#     i = 0
#     while i < len(s):
#         if s[i] != " ":
#             temp += s[i]
#         elif s[i] == " " and temp != "":
#             ans = temp + " " + ans
#             temp = ""
#         i += 1
#     # Add the last word to the result if it's not empty
#     if temp != "":
#         ans = temp + " " + ans
#         temp = ""
#     return ans.strip()  # Remove trailing space if any

# ----------------------------------------------
# problem-4
#  def largestOddNumber(self, num: str) -> str:
# ---------------------------converting string to integer consumes more time (drawback of this approach)
        # mx = 0
        # if int(num[-1]) % 2 != 0:
        #     return num
        # for i in range(len(num)):
        #     ans = ""
        #     for j in range(i,len(num)):
        #         ans += num[j]
        #         if (int(ans[-1]) % 2) != 0:
        #             mx = max(mx,int(ans))
        # if mx != 0:
        #     return str(mx)
        # else:
        #     return ""
    # ----------------effective approach than above one ---------------------
        # for i in range(len(num)-1,-1,-1):
        #     if ord(num[i]) % 2 != 0:
        #         return num[:i+1]
        # return ""
