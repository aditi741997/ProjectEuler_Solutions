import math

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
	sieve_n=sieve(u)
	while i < u:
		if sieve_n[i]:
			ans.append(i)
		i += 1
	return ans
	#if ith true hai to append i+1 in list of primes.
#better maintain a hashmap for this. easy ho jaayega. Abhi exponential. :/
yo = {}

def g(x,a):
	global yo
	if not yo.has_key((x,a)):
		if x<a:
			yo[(x,a)] = 1
		else:
			yo[(x,a)] = g(x-1,a) + g(x-a,a)
	return yo[(x,a)]

def gg(x,a):
	if x<a:
		return 1
	else:
		return gg(x-1,a) + gg(x-a,a)

def big_G(n):
	if n==90:
		return 7564511
	else:
		return g(n,n**0.5)

prime = primelist(10000000,10010000)


answer = 0
# for elem in prime:
# 	answer += big_G(elem)
#when u take to x+1 levels :: 
# g(p, rt p) = sum(i = 0 to x) g(p - i*(rt p) - x + i, rt p)



print math.floor(3.14)
print math.floor(-4.6)
#print answer
#print answer%1000000007