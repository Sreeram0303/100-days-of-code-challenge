# //  -------------------------------
# // problem-1

# // #include<iostream>
# // #include<vector>
# // #include <algorithm>
# // using namespace std;
# // int happyKids(vector<int> &balls) {
# //     // Write your code here.
# //     int n = balls.size();
# //     sort(balls.begin(),balls.end());
# //     for(int i=n-1;i>=1;i--){
# //         if(balls[i] == balls[i-1]){
# //             return balls[i];
# //         }
# //     }
# //     return -1;
# // }

# ------------------------------------------
# problem-2

# def productionHouse(n: int, m: int, days: List[int], needs: List[int]) -> int:
#     # Write your code here.
#     HM = {}
#     for i in range(m):
#         HM[days[i]] = needs[i]
#     HM = sorted(HM.items())
#     sold = 0
#     for i in range(m):
#         if ((n*HM[i][0])-sold) < HM[i][1]:
#             return 0
#         sold += HM[i][1]
#     return 1

# --------------------------------------
# problem-3

# def farmingGame(n, m, x, r, c):
#     columns = [[] for _ in range(n + 1)]

#     for i in range(x):
#         columns[r[i]].append(c[i])

#     maxCrops = 0
#     minCrops = 0

#     for i in range(1, n + 1):
#         columns[i].sort()
#         columns[i].append(m + 1)

#         prev = 0

#         for j in range(len(columns[i])):
#             len_crops = columns[i][j] - prev - 1

#             maxCrops += (len_crops + 1) // 2
#             minCrops += (len_crops + 2) // 3
#             prev = columns[i][j]

#     return [maxCrops, minCrops]
