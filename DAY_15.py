# ---------------------------------------------------#
# Problem - 1

# Majority Element (floor of n/3)

# from typing import List
# def majorityElement(self, v: List[int]) -> List[int]:
        # HM = {}-----------------------------------------------
        # for i in range(len(v)):
        #     if v[i] in HM:
        #         HM[v[i]] += 1
        #     else:
        #         HM[v[i]] = 1
        # j = []
        # for x,y in HM.items():
        #     if y > len(v) //3:
        #         j.append(x)
        # return j------------------------------------------------
        # Write your code here
        # HM = defaultdict(lambda:0)
        # j = []
        # for i in v:
        #     HM[i]+=1
        #     if HM[i] == (len(v)//3)+1:
        #         j.append(i)
        # j.sort()
        # return j
          # # Write your code here------------------------------
          # HM = {}
          # for i in range(len(v)):
          #     if v[i] in HM:
          #         HM[v[i]] += 1
          #     else:
          #         HM[v[i]] = 1

          # j = []
          # for x,y in HM.items():
          #     if y > len(v) //3:
          #         j.append(x)
          # j.sort()
          # return j
        #   ----------------------------Optimal solution
        # cnt1 = 0
        # cnt2 = 0
        # ele1 = None
        # ele2 = None
        # for i in range(len(v)):-------------------Used the same voting algorithm which is used for n//2 majority element but for 2 elements with slight changes
        #     if cnt1==0 and v[i] != ele2:
        #         ele1 = v[i]
        #         cnt1 = 1
        #     elif cnt2 == 0 and v[i] != ele1:
        #         ele2 = v[i]
        #         cnt2 = 1
        #     elif ele1 == v[i]:
        #         cnt1 += 1
        #     elif ele2 == v[i]:
        #         cnt2 += 1
        #     else:
        #         cnt1 -= 1
        #         cnt2 -= 1
        # cnt1 = 0
        # cnt2 = 0 
        # j = []
        # for i in range(len(v)):
        #     if ele1 == v[i]:
        #         cnt1 += 1
        #     if ele2 == v[i]:
        #         cnt2 += 1
        # if cnt1 >= (len(v) // 3) + 1:
        #     j.append(ele1)
        # if cnt2 >= (len(v)//3)+1:
        #     j.append(ele2)
        # j.sort()
        # return j

# ---------------------------------------------------#

# Problem - 2
# 3 SUM
# def triplet(n: int, arr: [int]) -> [[int]]:------------BRUTE FORCE
    # # Write your code here.
    # ans = []
    # for i in range(n):
    #     for j in range(i+1,n):
    #         for k in range(j+1,n):
    #             if arr[i]+arr[j]+arr[k] == 0:
    #                 ls =[arr[i],arr[j],arr[k]]
    #                 ls.sort()
    #                 if ls not in ans:
    #                     ans.append(ls)

    # return ans
# def triplet(n, arr):-----------BETTER SOL
#     ans =[]

#     for i in range(n):
#         HM = {}
#         for j in range(i + 1, n):
#             # Calculate the 3rd element:
#             third = -(arr[i] + arr[j])

#             # Find the element in the set:
#             if third in HM.keys():
#                 temp = [arr[i], arr[j], third]
#                 temp.sort()
#                 if temp not in ans:
#                     ans.append(temp)
#             HM[arr[j]] = 0
#     # store the set in the answer:
    
#     return ans
# def triplet(n: int, arr: [int]) -> [[int]]:------------OPTIMAL SOL
#     arr.sort()
#     ans = []
#     for i in range(n):
#         if i > 0 and arr[i] == arr[i-1]:
#             continue
#         j = i + 1
#         k = n - 1
#         while j < k:
#             sum = arr[i] + arr[j] + arr[k]
#             if sum < 0:
#                 j += 1
#             elif sum > 0:
#                 k -= 1
#             else:
#                 temp = [arr[i],arr[j],arr[k]]
#                 ans.append(temp)
#                 j += 1
#                 k -= 1
#                 while j < k and arr[j] == arr [j-1]:
#                     j += 1
#                 while j < k and arr[k] == arr [k+1]:
#                     k -= 1

#     return ans
# --------------------------------------------
# def fourSum(nums: [int], target: int) -> [[int]]:--------BRUTE FORCE
    # Write your code from here.
    # cnt = 0
    # ans = []
    # n = len(nums)
    # for i in range(n):
    #     for j in range(i+1,n):
    #         for k in range(j+1,n):
    #             for l in range(k+1,n):
    #                 if nums[i]+nums[j]+nums[k]+nums[l] == target:
    #                     temp = [nums[i],nums[j],nums[k],nums[l]]
    #                     temp.sort()
    #                     if temp not in ans:
    #                         cnt += 1
    #                         ans.append(temp)
        
    # return ans
    # ans = []
    # n = len(nums)---------------------------better solution
    # for i in range(n):
    #     for j in range(i+1,n):
    #         HM = {}
    #         for k in range(j+1,n):
    #             sum = nums[i]+nums[j]+nums[k]
    #             rem = target - sum
    #             if rem in HM.keys():
    #                 temp = [nums[i],nums[j],nums[k],rem]
    #                 temp.sort()
    #                 if temp not in ans:
    #                     ans.append(temp)
    #             HM[nums[k]] = 0
    # return ans
    # n = len(nums) # size of the array
    # ans = []

    # # sort the given array:
    # nums.sort()

    # # calculating the quadruplets:
    # for i in range(n):
    #     # avoid the duplicates while moving i:
    #     if i > 0 and nums[i] == nums[i - 1]:
    #         continue
    #     for j in range(i + 1, n):
    #         # avoid the duplicates while moving j:
    #         if j > i + 1 and nums[j] == nums[j - 1]:------OPTIMAL SOLUTION
    #             continue

    #         # 2 pointers:
    #         k = j + 1
    #         l = n - 1
    #         while k < l:
    #             _sum = nums[i] + nums[j] + nums[k] + nums[l]
    #             if _sum == target:
    #                 temp = [nums[i], nums[j], nums[k], nums[l]]
    #                 ans.append(temp)
    #                 k += 1
    #                 l -= 1

    #                 # skip the duplicates:
    #                 while k < l and nums[k] == nums[k - 1]:
    #                     k += 1
    #                 while k < l and nums[l] == nums[l + 1]:
    #                     l -= 1
    #             elif _sum < target:
    #                 k += 1
    #             else:
    #                 l -= 1

    # return ans





