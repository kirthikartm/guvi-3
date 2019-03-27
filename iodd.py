try:
    n=input()
    n=n.split()
    l=[]
    for i in n:
        t=int(i)
        l.append(t)
    a=l[0]
    b=l[1]
    k=[]
    for j in range(a+1,b):
        if(j%2!=0):
            k.append(j)
    for i in range(len(k)-1):
        print(k[i],end=' ')
    print(k[-1])
except:
    print("invalid")
