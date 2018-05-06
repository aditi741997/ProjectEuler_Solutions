# trying euler 124. HM of rad n
rad = []
for i in xrange(0,100000,1):
	rad.append(0)

print len(rad)

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

plist = primelist(1,100000)

print "Primes ready, starting rad."

# now fill rad.
rad[0] = 1

for elem in plist:
	rad[elem-1] = elem

for i in xrange(3,100000,1):
	if rad[i] == 0:
		# find the first prime divisible by i
		x = 0
		j = i+1
		while not j%plist[x] == 0:
			x += 1
		# found. plist[x] divides i
		p1 = plist[x]
		if (j/p1)%p1 == 0:
			rad[i] = rad[j/p1 - 1]
		else:
			rad[i] = rad[j/p1 - 1]*p1

print "All rads done."
print rad[7]
print rad[503]
print rad[10000]
# traverse rad, sort all.

# sorting main problem!!