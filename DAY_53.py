    # ----------------------------------------
    # problem-1

    # def solve(ind,s,ds,ans):
    #     if ind == len(s):
    #         check = "".join(ds)
    #         if check not in ans:
    #             ans.append(check)
    #         return
    #     ds.append(s[ind])
    #     solve(ind+1,s,ds,ans)
    #     ds.pop()
    #     solve(ind+1,s,ds,ans)
    #     return

    # def moreSubsequence(n: int, m: int, a: str, b:str) -> str:
    #     # Write your code here.
    #     ans1 = []
    #     ans2 = []
    #     ds1 = []
    #     ds2 = []
    #     solve(0,a,ds1,ans1)
    #     solve(0,b,ds2,ans2)
    #     if len(ans1) >= len(ans2):
    #         return a
    #     else:
    #         return b

    # ----------------------------------------
    # problem-2

    # from typing import List
    # def partition( s: str) -> List[List[str]]:
    #         res = []
    #         path = []
    #         def partitionHelper(index: int):
    #             if index == len(s):
    #                 res.append(path[:])
    #                 return
    #             for i in range(index, len(s)):
    #                 if isPalindrome(s, index, i):
    #                     path.append(s[index:i + 1])
    #                     partitionHelper(i + 1)
    #                     path.pop()
    #         def isPalindrome(s: str, start: int, end: int) -> bool:
    #             while start <= end:
    #                 if s[start] != s[end]:
    #                     return False
    #                 start += 1
    #                 end -= 1
    #             return True
    #         partitionHelper(0)
    #         return res