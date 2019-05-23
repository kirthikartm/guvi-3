n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in range(0,n):
    if i==l[i]:
        l1.append(i)
for i in l1:
    print(i,end=" ")
if(len(l1)==0):
    print("-1")
