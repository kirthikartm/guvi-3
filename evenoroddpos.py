n=int(input())
l=list(map(int,input().split()))
for i in range(0,n):
    if i%2==0:
        if l[i]%2!=0:
            print(l[i],end=" ")
    elif i%2!=0:
        if l[i]%2==0:
            print(l[i],end=" ")
