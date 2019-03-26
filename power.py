try:
    n=input()
    n=n.split()
    l=[]
    for i in n:
        t=int(i)
        l.append(t)
    a=l[0]
    b=l[1]
    print(pow(a,b))
except:
    print("invalid")
