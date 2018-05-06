# function to check if 2 numbers are anagrams.
# euler 62
		VERY VERY SLOW!!
def AreAnagrams(n1,n2):
	HM1 = {}
	HM2 = {}
	str1 = str(n1)
	str2 = str(n2)
	if len(str1) == len(str2):
		n = len(str1)
		for i in xrange(1,n,1):
			ith = int(str1[i])
			if not HM1.has_key(ith):
				HM1[ith] = 1
			else:
				HM1[ith] += 1

		for i in xrange(1,n,1):
			ith = int(str2[i])
			if not HM2.has_key(ith):
				HM2[ith] = 1
			else:
				HM2[ith] += 1
		# 2 hashmaps ready.
		i = 0
		rthis = True
		while i < n and rthis:
			ith = int(str2[i])
			if HM1.get(ith) != HM2.get(ith):
				rthis = False
			i += 1
		return rthis
	else:
		return False

# find totient of numbers

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

Primes = primelist(1,10000000)
totalPrimes = len(Primes)

# totient using primes in Primes.
def Totient(n):
	global Primes
	global totalPrimes
	i = 0
	ans = n
	while i < totalPrimes and Primes[i] <= n/2:
		ith = Primes[i]
		if (n%ith == 0):
			ans /= ith
			ans *= (ith - 1)
		i += 1
	if ans == n and ans != 1:
		return ans - 1
	else:
		return ans

print Totient(1)
globalminTot = 0 # min ratio
min_no = 1
for i in xrange(1,10000000,1):
	x = Totient(i)
	if AreAnagrams(i,x):
		if i*globalminTot <= x*min_no:
			globalminTot = x
			min_no = i

print min_no

