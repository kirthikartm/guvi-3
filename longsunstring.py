n=input()
s=len(n)
for i in range(s):
    sub=n[i::]
    if sub[0]>n[0]:
        print(sub)
        break
