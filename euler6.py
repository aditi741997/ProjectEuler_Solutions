def sum_sq(n):
    return n*(n+1)*(2*n+1)/6

def sq_sum(n):
    return pow(n*(n+1)/2,2)



print sum_sq(10) - sq_sum(10)
print sum_sq(100) - sq_sum(100)
