# euler 67
# read file.
# make matrix: 100 by 100
f = open('p067_triangle.txt','r')
# an array of vectors.
V_Arr = [[]]*100
i = 0
for line in f:
	V_Arr[i] = line.split(' ')
	for j in xrange(0,i+1,1):
		V_Arr[i][j] = int(V_Arr[i][j])
	i += 1

for i in xrange(98,-1,-1):
	for j in xrange(0,i+1,1):
		addthis = max(V_Arr[i+1][j],V_Arr[i+1][j+1])
		V_Arr[i][j] += addthis
		# print addthis, V_Arr[i][j]

for elem in V_Arr[0]:
	print elem