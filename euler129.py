# trying euler 129
# for n, continue till a div repunit found.
import time

t1 = time.time()

found = False
i = 0

while not found:
	i += 1
	while i%2 == 0 or i%5 == 0:
		i += 1
	
	rep = 1   #store just mod and nodig = R(rep)
	nodig = 1
	idiv = False
	while not idiv:
		if rep%i == 0:
			idiv = True
		else:
			if nodig > 1000000:
				found = True
				idiv = True
			else:
				nodig += 1
				rep = (10*rep + 1)%i
	if idiv and nodig > 1000000:
		found = True

t2 = time.time()

print i,nodig,t2-t1