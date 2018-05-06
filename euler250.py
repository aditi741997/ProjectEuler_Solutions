# euler250.
import time
t1 = time.time()

RemI = [0]*250250 # 1 to 250250 : i^i mod 250 = RemI[i-1]

Rem250 = [0]*125  # 1 to 125 : i^250 mod 250 = Rem250[i-1]
for i in xrange(0,125,1):
	Rem250[i] = pow(i+1,250,250)

# power 250 pata hai for all remainders
# RemI[0] = 1^1, RemI[1] = 2^2, RemI[249] = 0 (250^250)
for i in xrange(0,249,1):
	RemI[i] = pow(i+1, i+1,250)

for i in xrange(1,250,1):
	finalthis = i
	ans = RemI[i-1]
	while finalthis < 250250:
		RemI[finalthis - 1] = ans
		if i < 126:
			ans = (ans*Rem250[i-1])%250
		else:
			ans = (ans*Rem250[250-i-1])%250
		finalthis += 250
# i = 125 -> Rem250[124]. i =126 => Rem250[124].
print RemI[250], RemI[2278], RemI[28] #(251^251, 280^280, 30^30)
print pow(29,2279,250)

NoRem = [[0 for x in range(250)] for x in range(2)]

# assume empty set to be a subset.

NoRem[1][0] = 2
print "Preliminary work done"


for xfinal in xrange(250248,-1,-1):
	# subset from xfinal + 1 to 250250.
	for nfinal in xrange(0,250,1):
		NoRem[0][nfinal] = NoRem[1][nfinal] + NoRem[1][(nfinal - RemI[xfinal])%250]
	NoRem[1] = NoRem[0]
	t3 = time.time()
	if xfinal%250 == 0:
		print xfinal, t3-t1

t2 = time.time()

print NoRem[0], t2-t1