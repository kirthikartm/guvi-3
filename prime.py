try:
    n=int(input())
    if n>1:
        for i in range(2,n//2):
            if(n%i)==0:
                f=1
                break
            else:
                f=0
    else:
        print("no")
    if(f==0):
        print("yes")
    else:
        print("no")
except:
    print("invalid")
