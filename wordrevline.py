n=input()
n=n.split()
l=[]
for i in n:
    l.append(i)
x=""
for i in range(0,len(l)):
    x=l[i]
    l[i]=x[::-1]
for i in l:
    print(i,end=" ")
