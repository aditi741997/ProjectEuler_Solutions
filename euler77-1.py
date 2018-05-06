
def sieve(n):
	j=2
	k=0
	yolist=[1]*n
	while j**2<n:
		k=j**2
		while k<n:
			yolist[k]=0
			k += j
		j += 1
		while yolist[j]==0:
			j += 1
	return yolist

# 1 = true,0 = false

def primelist(l,u):
	i = l
	ans=[]
	sieve_n=sieve(u + 1)
	if i == 1:
		i = 2
	while i <= u:
		if sieve_n[i]:
			ans.append(i)
		i += 1
	return ans

plist = primelist(1,50000)
x = len(plist)

a = {}
