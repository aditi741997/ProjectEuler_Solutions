#euler 77
# list of primes till some no. : LET 5000 primes.
# table of n*5000, 

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

plist = primelist(1,50000)
x = len(plist)

pn = [0,0,1] # store F(n,largest prime less than n) in pn. pn[n] = #ways for n.

maxp = [0,0,0,1]

a0 = []
for x in xrange(0,x):
	a0.append(0)

a1 = []
for x in xrange(0,x):
	a1.append(1)

a3 = [0,1]
for x in xrange(0,x-2):
	a3.append(1)

print len(a3)

FNP2 = []
for i in xrange(0,1000,1):
	FNP2.append(a0)

FNP2[2] = a1
FNP2[3] = a3

# F(n,Pi) = F(n-Pi, Pi) + F(n,P i-1)
print FNP2[1][1]

for i in xrange(4,1000):
	a = FNP2[i]
	# append a to FNP2 in end.
	if i%2 == 0:
		FNP2[i][0] = 1
	# else:
	# 	FNP2[i][0] = 0
	# print i
	for j in xrange(1,x,1):
		pj = plist[j]
		# print "pj is:", pj
		if i>pj:
			# if i-pj
			if maxp[i-pj] < j:
				FNP2[i][j] = FNP2[i-pj][maxp[i-pj]] + FNP2[i][j-1]
			else:
				FNP2[i][j] = FNP2[i-pj][j] + FNP2[i][j-1]
				
			if i==9:
				print "i-pj: ", i - pj
				print "xx j: ", j
				print "i-pj,j : " , FNP2[i-pj][j]
		elif i == pj:
			FNP2[i][j] = FNP2[i][j-1] + 1
		else:
			m = FNP2[i][j-1]
			FNP2[i][j] = m
			pn.append(m)
			maxp.append(j-1)
			j = x
		# s = "i :" + i + ", j : " + j + " val " +FNP2[i][j]
		if i == 9 and j < 20:
			print "i : ", i
			print ", j :", j-1
			print " val:", FNP2[i][j-1]
  
print FNP2[2][2]
print " n=3: ", FNP2[3][3]
print " n=10: ", FNP2[10][10]