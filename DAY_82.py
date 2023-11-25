# problem - 1
# def findTimeToReach(n: int, a: int, b: int) -> int:
#     # Write your code here. 
#     n = n - 1
#     time = a * 10
#     if b <= n and a < b:
#         time += (b-a)*10
#     elif b<=n and a > b:
#         time += ((n-a)*10 + (n-b)*10)
#     return time

# problem - 2
# def findWinner(n : int , m : int) -> str:
#     # Write your code here.
#     if (n // m) % 2 == 0:
#         return "BOB"
#     else:
#         return "ALICE"

# problem-3
# def canYouGetSame(n: int, m: int, S: str, T: str):
#     ptr_s, ptr_t = 0, 0
#     while ptr_s < len(S) and ptr_t < len(T):
#         if S[ptr_s] == T[ptr_t]:
#             ptr_s += 1
#             ptr_t += 1
#         else:
#             ptr_s += 1
#             if ptr_s < len(S) and S[ptr_s] == S[ptr_s - 1]:
#                 ptr_s += 1
#     return 1 if ptr_t == len(T) else 0