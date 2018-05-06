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

yo = primelist(1,29)
for elem in yo:
	print elem

yo = primelist(1,1000000)
no_primes = len(yo);

LP = {}
NoPrimeAdded = [1]*no_primes

for elem in yo:
	LP[elem] = elem

for i in xrange(0,no_primes,1):
	curr_prime = yo[i]
	curr_sum = curr_prime
	y = i + 1;
	while curr_sum < 1000000 and y < no_primes:
		curr_sum += yo[y]
		if LP.has_key(curr_sum):
			NoPrimeAdded[i] = y - i
			LP[curr_prime] = curr_sum
		# else mein kya?
		y += 1
	# Done with ith prime

# got values for longest conti prime sum starting from ith prime

max_no_posn = 1
curr_max = 0
for i in xrange (0,no_primes,1):
	if NoPrimeAdded[i] > curr_max:
		max_no_posn = i
		curr_max = NoPrimeAdded[i]

print curr_max
print LP[yo[max_no_posn]]