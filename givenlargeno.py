x,y=map(int,input().split())
a=list(map(int,input().split()))
s=sorted(a)
s=s[::-1]
print(s[y-1])
    
