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

def primes(l):
	yoyo=sieve(l+1)
	ans=[]
	y=2
	while y<=l:
		if yoyo[y]==1:
			ans.append(y)
		y += 1
	return ans

def nonprimes(l,u):
	yoyo=sieve(u+1)
	ans=[]
	y=l
	while y<=u:
		if yoyo[y]==0 and y%2==1:
			ans.append(y)
		y += 1
	return ans

def int2list(n):
	alist=[n%10]
	if n>=10:
		while n>=10:
			n /= 10
			alist.append((n%10))
	alist.reverse()
	return alist

def checkprime2(n):
	start=True
	if n==2:
		start=True
	else:
		if n%2==0:
			start=False
		else:
			k=3
			while k<=(n**0.5) and start==True:
				if n%k==0 and checkprime2(k):
					start=False
				k += 2
	return start

def listneed(n,l):
	yoyo=sieve(l+1)
	ans=0
	y=2
	while y<=l and ans<l:
		if yoyo[y]==1:
			ans += 1
		y += 1
	return y
#trying 49 here!
def p2list(l):
	yo=[]
	for elem in l:
		yo.append(int2list(elem))
	return yo

# def sublist(l1,l2):
# 	answer=True
# 	for elem in l1:
# 		answer&= elem in l2
# 	return answer

# def eqlist(l1,l2):
# 	return sublist(l1,l2) and sublist(l2,l1)
 #eqlist should NOT RETURN TRUE FOR: [2,3,2] and [2,3,3]

import collections
compare = lambda x,y: collections.Counter(x)==collections.Counter(y)

print compare([2],[23])
print compare([3,7],[7,3])

def list2int(l):
	i=0
	a=0
	y=len(l)
	while i<y:
		a += l[i]*(10**(y-i-1))
		i += 1
	return a

print list2int([1,2,3,4])
print list2int([2,3])
print len(primes(1000))

def perm_list(n):
	this_isit=[]
	l=primes(n)[168:]
	use_this=p2list(l)
	z=len(use_this)
	while z>0:
		m=use_this[0]
		i=1
		ith_combo=[list2int(m)]
		while i<z:
			y=use_this[i]
			if compare(m,y):
				ith_combo.append(list2int(y))
				use_this= use_this[0:i] + use_this[i+1:]
				z=len(use_this)
			i += 1
		if len(ith_combo)>1:
			this_isit.append(ith_combo)
		use_this = use_this[1:]
		z=len(use_this)
	yo=[]
	for elem in this_isit:
		if len(elem)>=3:
			yo.append(elem)
	yoy=[]
	yo = yo[30:]
	for elem in yo:
		i=0
		z=len(elem)
		while i<z:
			j=i+2
			if j<z:
				while j<z:
					w=(elem[i]+elem[j])/2
					if w in elem:
						yoy.append([elem[i],elem[j],w])
					j += 1
			i += 1
	return yoy

print perm_list(10000)