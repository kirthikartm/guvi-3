n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        if(l[i]==l[j]):
            l1.append(l[i])
l2=list(set(l)^set(l1))
for i in l2:
    print(i,end=" ")
