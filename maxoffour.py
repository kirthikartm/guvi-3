n,x,y,z=map(int,input().split())
a=list(map(int,input().split()))
s=0
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i<=j<=k:
                b=x*a[i]+y*a[j]+z*a[k]
            if b>s:
                s=b
print(s)
