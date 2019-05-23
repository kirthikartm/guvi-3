z=int(input())
n=input()
n=n.split()
l=[]
for i in n:
    t=int(i)
    l.append(t)
l.sort(reverse=True)
for i in l:
    print(i,end="")
