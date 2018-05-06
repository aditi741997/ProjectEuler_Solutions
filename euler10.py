import time

def sievesum(n):
	k=2
	summy=0
	while k<n:
		if checkprime2(k):
			summy += k
		k += 1
	return summy

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
	#if ith true hai to append i+1 in list of primes.

# no_of_tests = int(raw_input())
# x = 0
# mn = []
# while x < no_of_tests:
# 	# ranger = raw_input()
# 	x += 1
# 	# divide range by space
# 	lu = map(int, raw_input().split())
# 	lower = lu[0]
# 	upper = lu[1]
# 	m = primelist(lower, upper)
# 	for elems in m:
# 		mn.append(elems)
# 	if x <= no_of_tests - 1:
# 		mn.append(-1)

# for yoy in mn:
# 	if yoy > -1:
# 		print yoy
# 	else:
# 		print "\n"

def sumsieve(n):
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
	sun=0
	m=2
	while m<n:
		if yolist[m]==1:
			sun += m
		m += 1
	return sun


t1=time.time()
print sumsieve(2000000)
t2=time.time()
print t2-t1

# print sieve(30)

yo = primelist(1, 11)
for elem in yo:
	print elem


