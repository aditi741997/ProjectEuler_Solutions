# trying euler 78.
# T(n,k) = sigma(i : 1 to [n/k]) T(n - (i-1)(k-1) - i, k)

# k from 1 to n.
# Python. HM??
import time
import math

a = {}

a[(1,1)] = 1

n = 1
Sn = 1   # i=1 ka no ways. mod 10**6

t1 = time.time()

while not Sn%1000000 == 0:
	n += 1
	Sn = 0
	for k in xrange(1,n+1,1):
		# a[(i,k)] to be found.
		a[(n,k)] = 0
		if k == n:
			a[(n,k)] = 1
		else:
			if k == 1:
				a[(n,k)] = 1
			else:
				if k == 2:
					a[(n,k)] = n/k
				else:
					for i in xrange(1,n/k + 1,1):
						a[(n,k)] = (a[(n,k)] + a[(n - 1 - i*k + k,k-1)])%1000000
		Sn = (Sn + a[(n,k)])%1000000
	t3 = time.time()
	if n%100 == 6:
		print n, Sn, t3 - t1

t2 = time.time()
print "Done"
print n, Sn, t2 - t1