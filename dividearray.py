n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(0,len(l)):
    c=c+1
if c%2==0:
    print("no")
else:
    print("yes")
