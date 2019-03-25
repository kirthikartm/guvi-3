try:
    n=input()
    n=n.split()
    a=n[0]
    b=n[1]
    c=n[2]
    if a>b and a>c:
        print(a)
    elif b>a and b>c:
        print(b)
    else:
        print(c)
except:
    print("invalid")
