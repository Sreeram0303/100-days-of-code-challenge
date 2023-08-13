#problem-1
def findX(arr):
    # write your code here
    HM = {}
    for i in range(len(arr)):
        HM[arr[i]] = 1
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] == arr[j] and arr[j] != -1:
                HM[arr[i]] += 1
                arr[j] = -1
    mx = -1
    ele = 0
    for x,y in HM.items():
        if x == y and y > mx:
            mx = y
            ele = x
    return ele
#problem-2
def totalIndexes(A, B):
    # write your code here
    def dic(HM,A):
        suml=0
        for i in range(len(A)):
            suml += A[i]
            sumr=0
            for j in range(i+1,len(A)):
                sumr += A[j]
            if suml == sumr and i != len(A)-1:
                HM[i] = suml
    HMA = {}
    HMB = {}
    dic(HMA,A)
    dic(HMB,B)
    count = 0
    # print(HMA,HMB,sep='-')
    for x,y in HMA.items():
        for i,j in HMB.items():
            if x == i and y == j:
                count += 1
    return count
            
