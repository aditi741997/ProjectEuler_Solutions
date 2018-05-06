#reverse add f, then for all nos -> HashMap. (n, atmost m steps) : true/false : tuple -> bool
#after ith iter the no we get: can that be made to pal in 49-i ?

a = {}



def g(n):
	global a
	if not a.has_key(n):
		

# yo gives reverse of n.
def yo(n):
	m = n
	yo = []
	while m>=10:
		yo.append(m%10)
		m = m/10
	yo.append(m)
	i = 0
	ans = 0
	leng = len(yo)
	while i<leng:
		ans += yo[i]*(10**(leng - i -1))
		i += 1
	return ans

#  PALINDROME? yo(n) == n
count = 0
for i in xrange(1,10000,1):
	if g(i) <50:
		count += 1

print count

print yo(17)
print yo(20)
print yo(21)
print yo(450)
print yo(789)