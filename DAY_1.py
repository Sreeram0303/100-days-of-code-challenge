# PROBLEM - 1 (link)
# LINK - https://www.codingninjas.com/studio/problems/if-else-decision-making_8357235?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
# CODE:
# from typing import *
# def compareIfElse(a: int, b: int):
#     # Write your code here
#     if a > b:
#         return 'greater'
#     elif b > a:
#         return 'smaller'
#     else:
#         return "equal"
#     pass

# PROBLEM - 2
# LINK - https://www.codingninjas.com/studio/problems/nth-fibonacci-number_74156?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
# CODE:
# from math import *
# from collections import *
# from sys import *
# from os import *
# ## Read input as specified in the question.
# N = int(input())
# # ## Print output as specified in the question.
# # def fib(N):                                                 
# #     if N == 0:
# #         return 0
# #     if N == 1:
# #         return 1
# #     fiba = fib(N-1) + fib(N-2)
# #     return fiba
# # res = fib(N)
# # print(res)
# fib = [1,1]
# for i in range(2,N):
#     fib.append(fib[i-1]+fib[i-2])
# print(fib[N-1])

#PROBLEM - 3 (link)
#https://www.codingninjas.com/studio/problems/sum-of-even-odd_624650?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
#CODE:
## Note : For printing multiple values in one line, put them inside print separated by space.
## You can follow this syntax for printing values of two variables val1 and val2 separaetd by space -
## print(val1, " ", val2)
# n = int(input())
# sume = 0
# sumo = 0
# i = 0
# while i < len(str(n)):
#     if int(list(str(n))[i]) % 2 == 0:
#         sume +=  int(list(str(n))[i])
#     else:
#         sumo += int(list(str(n))[i])
#     i += 1
# print(sume,sumo,sep=" ")