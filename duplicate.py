z=int(input())
n=input()
n=n.split()
l=[]
for i in n:
    t=int(i)
    l.append(t)
l1=[]
for j in l:
    l1.append(j)
l2=[]
for i in range(0,len(l1)):
    for j in range(i+1,len(l)):
        if(l1[i]==l1[j]):
            l2.append(l1[i])
else:
    print("unique")
l2.sort()
l2=list(set(l2))
for i in l2:
    print(i,end=" ")
