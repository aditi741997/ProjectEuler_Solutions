# prime : val = 1
# otherwise : sigma ( F(divisors != 1,n))
import time;
t1 = time.time();


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

plist = primelist(1,10**7)

print len(plist)
# cant find primes till 10**16 as such.

gn = {}
gn[1] = 1
for elem in plist:
	gn[elem] = 1
gn[4] = 2
# initial primes covered.

def f(n):
	global gn
	if not  gn.has_key(n):
		x = 0
		for x in (2,(n/2) + 3):
			if (n%x == 0):
				x += f(x)
		gn[n] = x
	return gn[n]

such_no = 0;
for i in xrange(1,10**8):
	if f(i) == i:
		such_no += i


t2 = time.time();
print such_no
print "time : ", t2 - t1