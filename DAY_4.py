#problem-1
from typing import List
def printNos(x: int) -> List[int]: 
    # Write your code here
    if x <= 0:
        j = []
        return j
    j = printNos(x-1)
    j.append(x)
    return j
print(printNos(5))
#problem-2 
from  typing import *
def printNtimes(n: int) -> None:
    if n <= 0:
        j=""
        return j
    print('Coding Ninjas ',end='')
    printNtimes(n-1)
printNtimes(5)
print()
#problem-3
from typing import List

def printNos(x: int) -> List[int]:
    # Write your code here
    if x <= 0:
        
        return []
    j = printNos(x-1)
    j.insert(0,x)
    return j
print(printNos(5))

#problem-4
def fact(n):
    if n == 1 or n == 0:
        return 1
    return n*fact(n-1)
print(fact(5))
from typing import *
def fact(n):
    if n == 1 or n== 0:
        return 1
    
    return n*fact(n-1)
def factorialNumbers(n: int) -> List[int]:
    
    j = []
    for i in range(1,n+1):
        if fact(i) <= n:
            j.append(fact(i))
    return j
    
    
print(factorialNumbers(2))
#problem_5
def isPalindrome(string: str) -> bool:
    
    for i in range(0,len(string)//2):
        if string[i] != string[len(string)-i-1]:
            return False
    return True
#problem_6
def generateFibonacciNumbers(n: int) -> List[int]: 
    # Write your code here
    def fibo(n):
        if n==0:
            return 0
        elif n==1:
            return 1
        return fibo(n-1)+fibo(n-2)
    j= []
    for i in range(n+1):
        j.append(fibo(i))
    return j
print(generateFibonacciNumbers(5))
    


    
