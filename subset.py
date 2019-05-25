a=input()
a=a.split()
l2=[]
for i in a:
    t=int(i)
    l2.append(t)
n=l2[0]
m=l2[1]
l=list(map(int,input().split()))
l1=list(map(int,input().split()))
flag=0
if(all(x in l for x in l1)):
    flag=1
if flag==1:
    print("YES")
else:
    print("NO")
