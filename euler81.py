# euler 81
f = open('p081_matrix.txt','r')

VArr = [[]]

i = 0
for line in f:
	VArr[i] = line.split(',')
	for j in xrange(0,80,1):
		VArr[i][j] = int(VArr[i][j])
	i += 1

# now process.
for i in xrange(78,-1,-1):
	# lets finish last row first.
	VArr[79][i] += VArr[79][i+1]

for m in xrange(78,-1,-1):
	# all other rows.
	