import sieve
n = 600851475143
sq_n = int(pow(n,0.5))
print "sq_n : ", sq_n
all_primes = sieve.sieve(sq_n+2)
for i in xrange(sq_n+1,2,-1):
    if all_primes[i] and n%i == 0:
        print "Found ", i

