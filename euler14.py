# tester=500000
# maxlength=1
# maxtester=2
# while (tester<=1000000):
# 	length=0
# 	origtester=tester
# 	while (tester != 1):
# 		if (tester %2 ==0):
# 			tester=tester/2;
# 		else:
# 			tester=(tester*3) +1;
# 		length+=1
# 	if (length>maxlength):
# 		maxlength=length
# 		maxtester=origtester
# 	tester=1+origtester

# print maxtester

import time
t1=time.time()
a={}
a[1]=1

def f(n):
	global a
	if not  a.has_key(n):
		if n%2==0:
			a[n]=f(n/2)+1
		else:
			a[n] = f(3*n +1) +1
	return a[n]

maxsofar=0
present=0
for i in xrange(1000000,1,-1):
	# print i
	k=f(i)
	if k>maxsofar:
		maxsofar=k
		present=i

t2=time.time()
print present,maxsofar
print t2-t1