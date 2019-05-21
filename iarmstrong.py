n=input()
n=n.split()
l=[]
for w in n:
    t=int(w)
    l.append(t)
x=l[0]
y=l[1]
z=[]
for i in range(x,y):
    k=0
    temp=i
    while(temp!=0):
        r=temp%10
        k=k+(r*r*r)
        temp=temp//10
    if(i==k):
        z.append(k)
for j in range(len(z)-1):
    print(z[j],end=' ')
print(z[-1])
