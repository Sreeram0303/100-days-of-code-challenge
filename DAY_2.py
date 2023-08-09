print("pattern-1")
for i in range(5):
    for j in range(5):
        print("*",end='')
    print()
print()
print("pattern-2")
for i in range(5):
    for j in range(i+1):
        print("*",end='')
    print()
print()
print("pattern-3")
for i in range(5):
    for j in range(i+1):
        print(i+1,end='')
    print()
print()
print("pattern-4")
for i in range(5):
    for j in range(i+1):
        print(j+1,end='')
    print()
print()
print("pattern-5")
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print("*",end='')
    print()
print()
print("pattern-6")
for i in range(5,0,-1):
    for j in range(i):
        print(j+1,end='')
    print()
print()
print("pattern-7")
k = 1
for i in range(5):
    for j in range(i+1):
        print(k,end=' ')
        k += 1 
    print()
print()
print("pattern-8")
for i in range(5):
    for j in range(5-i-1):
        print(" ",end='')
    for j in range(2*i+1):
        print("*",end='')
    for j in range(5-i-1):
        print(" ",end='')
    print()
print()
print("pattern-9")
for i in range(5,0,-1):
    for j in range(5-i,0,-1):
        print(" ",end='')
    for j in range(2*i-1):
        print("*",end='')
    for j in range(5-i,0,-1):
        print(" ",end='')
    print()
print()
print("pattern-10")
for i in range(5):
    for j in range(5-i-1):
        print(" ",end='')
    for j in range(i+1):
        print("*",end=' ')
    for j in range(5-i-1):
        print(" ",end='')
    print()
for i in range(5,0,-1):
    for j in range(5-i,0,-1):
        print(" ",end='')
    for j in range(i):
        print("*",end=' ')
    for j in range(5-i,0,-1):
        print(" ",end='')
    print()
print()
print("pattern-11")
for i in range(5):
    for j in range(i+1):
        print("*",end='')
    print()
for i in range(5-1,0,-1):
    for j in range(i):
        print("*",end='')
    print()
print()
print("pattern-12")
for i in range(5):
    if i % 2 == 0:
        start = 1
    else:
        start = 0
    for j in range(i+1):
        print(start,end=' ')
        start = 1 - start
    print()
print()
print("pattern-13")
N = 5
space = 2*(N-1)
for i in range(N):
    for j in range(i+1):
        print(j+1,end=' ')
    for l in range(space):
        print(" ",end=' ')
    for k in range(i+1,0,-1):
        print(k,end=' ')
    space -= 2
    print()
print()
print("pattern-14")
for i in range(N):
    for j in range(i+1):
        print(chr(j+ord("A")),end=' ') #ord() to find the ascii value of the character and chr() to find the ascii character of the given value
    print() 
print()
print("pattern-15")
for i in range(N,0,-1):
    for j in range(i):
        print(chr(j+ord("A")),end='')
    print()
print()
print("pattern-16")
k=0
for i in range(N):
    for j in range(i+1):
        print(chr(k+ord("A")),end='')
    k += 1
    print()
print()
print("pattern-17")
for i in range(N):
    for k in range(N-i-1):
        print(' ',end='')
    for j in range(i+1):
        print(chr(j+ord("A")),end='') 
    for l in range(i-1,-1,-1):
        print(chr(l+ord("A")),end='') 
    print()
print()
print("pattern-18")
for i in range(N):
    for j in range(i+1):
        print(chr(ord("A")+N-1-j),end=' ') 
    print() 
print()
print("pattern-19")
m=0
for i in range(N,0,-1):
    for j in range(i):
        print("*",end='')
    for k in range(2*m):
        print(" ",end='')
    for l in range(i):
        print("*",end='')
    m+=1
    print()

m=2*(N-1)
for i in range(N):
    for j in range(i+1):
        print("*",end='')
    for k in range(m):
        print(" ",end='')
    for l in range(i+1):
        print("*",end='')
    m-=2
    print()
print()
print("pattern-20")
m=2*(N-1)
for i in range(N):
    for j in range(i+1):
        print("*",end='')
    for k in range(m):
        print(" ",end='')
    for l in range(i+1):
        print("*",end='')
    m-=2
    print()
m=1
for i in range(N-1,0,-1):
    for j in range(i):
        print("*",end='')
    for k in range(2*m):
        print(" ",end='')
    for l in range(i):
        print("*",end='')
    m+=1
    print()
print()
# N = 5
print("pattern-21")
for i in range(N):
    if i == 0 or i == N-1:
        print("*"*N,end='')
        print()
    else:
        print("*",end='')
        # for j in range(N-2):
        print(" "*(N-2),end='')
        print("*",end='')
        print()
print()
print("pattern-22")
N = 4
for i in range((2*N)-1):
    for j in range((2*N)-1):
        top = i
        left = j
        right = (2*N)-2 - j
        down = (2*N)-2 - i
        print(N - min(min(top,down),min(right,left)),end='')
    print()