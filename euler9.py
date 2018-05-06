
for i in xrange(500):
    for j in xrange(500):
        s = pow(i,2) + pow(j,2)
        s_sq = int(pow(s,0.5))
        if s_sq*s_sq == s and (i+j+s_sq == 1000):
            print i,j,s_sq,"FOUND"

