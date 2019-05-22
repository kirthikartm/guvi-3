import math
l=[]
def pfactor(n):
    while n%2==0:
        l.append(2)
        n=n/2
    for i in range(3,int(math.sqrt(n))+1,2):
        while n%i==0:
            l.append(i)
            n=n/i
    if n>2:
        l.append(n)
n=int(input())
pfactor(n)
s=list(set(l))
s.sort()
for j in range(len(s)-1):
    print(s[j],end=' ')
print(s[-1])
