def is_palindrome(x):
    s = str(x)
    for i in xrange(len(s)/2+1):
        if s[i] != s[-1*i - 1]:
            return False
    return True


print is_palindrome(10)
print is_palindrome(0)
print is_palindrome(101)
print is_palindrome(111)
print is_palindrome(121)
print is_palindrome(1310)

ans = 1
for i in xrange(1000):
    for j in xrange(1000):
        if is_palindrome(i*j) and i*j > ans:
            print "UPdating : ", i*j
            ans = i*j
print ans
