# Problem - 1
# class Item:
#     def __init__(self, value, weight):
#         self.value = value
#         self.weight = weight

# class Solution:
#     def fractionalknapsack(self, W, arr, n):
#         arr.sort(key=lambda x: x.value / x.weight, reverse=True)
#         curWeight = 0
#         finalvalue = 0.0
#         for i in range(n):
#             if curWeight + arr[i].weight <= W:
#                 curWeight += arr[i].weight
#                 finalvalue += arr[i].value
#             else:
#                 remain = W - curWeight
#                 finalvalue += arr[i].value / arr[i].weight * remain
#                 break
#         return finalvalue

# problem - 2
# class Solution:
#     def JobScheduling(self, jobs,n):
#         jobs.sort(key=lambda x: x.profit, reverse=True)
#         maxi = jobs[0].deadline
#         for i in range(1, len(jobs)):
#             maxi = max(maxi, jobs[i].deadline)


#         slot = [-1] * (maxi + 1)
#         countJobs = 0
#         jobProfit = 0


#         for i in range(len(jobs)):
#             for j in range(jobs[i].deadline, 0, -1):
#                 if slot[j] == -1:
#                     slot[j] = i
#                     countJobs += 1
#                     jobProfit += jobs[i].profit
#                     break
#         return countJobs, jobProfit