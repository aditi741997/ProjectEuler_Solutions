# 145. big integers.
import time
			# VERY VERY SLOW.
def isReversible(n):
	if n%10 == 0:
		return False
	else:
		strN = str(n)
		strRev = ""
		l = len(strN)
		for i in xrange(0,l,1):
			strRev += strN[l - 1 - i]
		Rev = int(strRev)
		finalStr = str(n + Rev)
		finalLen = len(finalStr)
		rthis = True
		i = 0
		while i < finalLen and rthis:
			if int(finalStr[i])%2 == 0:
				rthis = False
			i += 1
		return rthis

Rcount = 0
t1 = time.time()
for i in xrange(1,1000000000,1):
	if isReversible(i):
		Rcount += 1
	else:
		print i
t2 = time.time()
print Rcount,t2 - t1