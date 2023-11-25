# problem - 1
# def MinimumCoins(V: int) -> List[int]:
#     # write your code here
#     ans = []
#     coins = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
#     n = 9
#     for i in range(n - 1, -1, -1):
#         while V >= coins[i]:
#             V -= coins[i]
#             ans.append(coins[i])

#     return ans


# problem - 2

# from typing import List

# class Meeting:
#     def __init__(self, start, end, pos):
#         self.start = start
#         self.end = end
#         self.pos = pos

# class Solution:
#     def maximumMeetings(self, n, s, e):
#         meet = [Meeting(s[i], e[i], i + 1) for i in range(n)]
#         meet = sorted(meet, key=lambda x: (x.end, x.pos))
#         answer = []
#         limit = meet[0].end
#         answer.append(meet[0].pos)
#         for i in range(1, n):
#             if meet[i].start > limit:
#                 limit = meet[i].end
#                 answer.append(meet[i].pos)
#         return len(answer)

