# -------------------------
# problem-1

# from typing import List

# def canYouReach(n: int, h: List[int]) -> int:
#     # Write your code here.
#     for i in range(n-1):
#         if abs(h[i+1] - h[i]) > 1:
#             return 0
#     return 1

# -------------------------
# problem-2 (Binary search model)

# from typing import List

# def findNumberOfWays(n: int, a: int, b: int, coins: List[int]) -> int:
#     # Sort the 'coins' list in non-decreasing order.
#     coins.sort()
    
#     # Initialize the result to 0.
#     ways = 0
    
#     # Iterate through the possible values of 'X'.
#     for x in range(coins[0], coins[n - 1] + 1):
#         # Count the number of piles with coins less than or equal to 'X'.
#         alice_piles = len([c for c in coins if c <= x])
#         bob_piles = n - alice_piles
        
#         # Check if the distribution of piles matches 'A' and 'B'.
#         if alice_piles == a and bob_piles == b:
#             ways += 1

#     return ways

#
     