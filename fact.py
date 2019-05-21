def facti(n):
	if(n==1 or n==0):
		return 1
	else:
		return n*facti(n-1)
n=int(input())
print(facti(n))
