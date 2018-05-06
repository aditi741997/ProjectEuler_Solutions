# // phi(n) nikaalo
# python
import time

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

def primelist(l):
	i = 3
	ans=[2]
	sieve_n=sieve(l)
	while i < l:
		if sieve_n[i]:
			ans.append(i)
		i += 1
	return ans

print primelist(19)


theseprimes = primelist(9051)
totalp = len(theseprimes)

def phi(n):
	ans = n
	ith = 0
	while ith<totalp and theseprimes[ith]<(n+3)/2:
		elem = theseprimes[ith]
		if n%elem == 0:
			ans *= (elem - 1)
			ans /= elem
		ith += 1
	if ans == n:
		return (n-1)
	else:
		return ans
	# pfac has all prime factors of n.

print phi(30)
print phi(7)
print phi(12)
print phi(94745*2)


# brute force is tooooo bad!
def find_smallest(k):
	t1 = time.time()
	yo = 6
	done = False
	while yo < k and done == False:
		if 94744*phi(yo) < (yo - 1)*15499*2:
			done = True
			return yo
		else:
			yo += 1
	t2 = time.time()
	if done == False:
		print "k is small "

print find_smallest(200000)
t2 = time.time()
# print t2 - t1

# WE NEED A BETTER METHOD
# phi(2*odd) = phi(odd)
# phi(2*even) = phi(even)

t1 = time.time()
def find_ith(n):
	yoyo = 9
	prod1 = 1
	prod2 = 1
	while yoyo > -1 and 94744*prod1 >= (15499)*(prod2 - 1):
		prod1 *= (theseprimes[yoyo] - 1)
		prod2 *= theseprimes[yoyo]
		yoyo -= 1
	if yoyo == totalp - 1:
		print "nhi hua"
	else:
		return prod2, yoyo	
#replace small prime by larger one, does ration increase?...phi increases surely,
print find_ith(2)

print phi(6469693230)
print 2*3*5*7*11*13*17*19*23*29

t2 = time.time()
print t2 - t1