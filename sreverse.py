a=input()
a=list(a)
l=len(a)
def reve(a,i):
    if l//2>i:
        a[i],a[l-i-1]=a[l-i-1],a[i]
        reve(a,i+1)
reve(a,0)
str=""
a=str.join(a)
print(a)
