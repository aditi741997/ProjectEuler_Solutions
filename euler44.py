# try 44. Pentagon no.s!!

PentaKey = {}
PentaVal = {}
for i in xrange(1,50001,1):
	j = i*(3*i - 1)/2
	PentaKey[j] = i
	PentaVal[i] = j


k = 0
j = 0
minDiff = PentaVal[50000]

for i in xrange(1,35000,1):
	found = False   #for this i.
	y = i + 1
	x = PentaVal[i]
	while not found and y < i + 2000:
		yth = PentaVal[y]
		# check if sum and diff are pentagon values.
		if PentaKey.has_key(yth + x) and PentaKey.has_key(yth - x):
			if yth - x < minDiff:
				k = i
				j = y
				minDiff = yth - x
				print k,j,minDiff
		y += 1

print "final values are: "
print k,j,minDiff