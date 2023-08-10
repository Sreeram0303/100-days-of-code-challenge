#PROBLEM_1
def countDigits(n: int) -> int:
    j = []
    count = 0
    k = n
    while n > 0:
        m = n % 10
        j.append(m)
        n = n // 10
    for i in range(len(j)):
        if   j[i] != 0 and k % j[i] == 0:
            count += 1
  
    return count

#PROBLEM_2
n=int(input())  
# taking n as a input 
## write your code !!
N = list(str(n))
N.reverse()
if(''.join(N) == str(n)):
    print('true') 
else:
    print('false') 
    
#PROBLEM_3
def calcGDC(a, b):
    while b:
        a, b = b, a % b
    return a

#PROBLEM_4
from os import *
from sys import *
from collections import *
from math import *
count = 0
sum = 0
n = int(input())
k = n
while(n>0):
    m = n % 10
    sum += m**len(str(k))
    n //=10
if sum == k:
    print("true")
else:
    print("false")

#PROBLEM_5
from math import *
from collections import *
from sys import *
from os import *
import math

## Read input as specified in the question.
n = int(input())

def prime(n):
    if n < 2:
        return "NO"
    for i in range(2,int(n**0.5)+1):
        if n % i ==0:
            return "NO"
    return "YES"
res=prime(n)
print(res)

#PROBLEM_6
# def sumOfAllDivisors(n: int) -> int:
#     # Write your code here
#     sum = 0
#     for i in range(1,n+1):
#         j = 1
#         while j <= i:
#             if i % j == 0:
#                 sum += j
#             j += 1
#     return sum
def sumOfAllDivisors(n: int) -> int:
    # Write your code here
    divisor_sum = [0] * (n + 1)
    
    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            divisor_sum[j] += i
    
    return sum(divisor_sum)



