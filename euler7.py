def checkprime(n):
	k=2
	start=True
	while k<=(n**0.5) and start==True:
	k += 1
	return start

print checkprime(17)

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

print checkprime2(17)
print checkprime2(37)
print checkprime2(64)
print checkprime2(77)
print checkprime2(121)
# checkprime2 NO MORE fails for squares of prime nos

def yoprime(m):
	n=1
	t=3
	while n<m:
		if checkprime2(t):
			n += 1
		t += 2
	return (t-2)

print mprime(3)
print mprime(1001)
print mprime(10001)