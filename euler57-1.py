# euler 57 in python

num = 3
den = 2
count = 0
ln = 1
ld = 1
y = 0
for i in xrange(0,999,1):
	y = num + 2*den
	den = num + den
	num = y
	str_n = str(num)
	str_d = str(den)
	if len(str_n) > len(str_d):
		count += 1

print count