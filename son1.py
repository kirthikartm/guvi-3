try:
    n=input()
    n=n.split()
    l=[]
    for i in n:
        t=int(i)
        l.append(t)
    l1=[]
    m=input()
    m=m.split()
    for i in m:
        t=int(i)
        l1.append(t)
    s=0
    r=l[1]
    for i in range(0,r):
        s=s+l1[i]
    print(s)
except:
    print("invalid")
