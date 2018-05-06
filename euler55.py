# hashmap needed - LYCHREL NUMBERS
# euler 55

No = {}

for i in xrange(1,5,1):
		No[i] = 1

def rev(n):
	a = str(n)
	no = len(a)
	b=""
	for i in xrange(0,no,1):
		b += a[no - i - 1]
	rthis = int(b)
	return rthis

def f(n,itern):
	if itern <51:
		next = n + rev(n)
		# print n,next
		# check if next is a palindrome
		if not No.has_key(n):
			if isPalin(next):
				No[n] = 1
				return itern
			else:
				nextval = f(next,itern+1)
				if nextval == -1:
					No[n] = -1
					return -1
				else:
					No[n] = nextval
					return 1 + nextval
		else:
			# n has a key
			if No[n] == -1:
				return -1
			else:
				y = itern + No[n]
				if y > 50:
					return -1
				else:
					return y
	else:
		return -1


def isPalin(n):
	s = str(n)
	nxtlen = len(s)
	is_palin = True
	i = 0
	while i <= nxtlen/2 and is_palin:
		if s[i] != s[nxtlen - i - 1]:
			is_palin = False
		i += 1
	return is_palin

print rev(13)
print rev(154)
print isPalin(11)
print isPalin(1111)
print isPalin(111)
count = 0
for i in xrange(1,10000,1):
	k = f(i,0)

for i in xrange(1,10000,1):
	l = No[i]
	if l == -1:
		count += 1
		print i,l

print count
