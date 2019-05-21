n=input()
n=n.split()
l=[]
for i in n:
    t=int(i)
    l.append(t)
a=l[0]
b=l[1]
c=0
for i in range(a,b+1):
    if i>1:
        for j in range(2,i):
            if(i%j)==0:
                break
        else:
            c=c+1
print(c)
