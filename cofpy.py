#!/usr/bin/python3
n = 1
poly = n ** 4
exp = 2 ** n
print('%12s%12s%12s' % ('n^4','2^n','n'))
while n < 50:
    poly = n ** 4
    exp = 2 ** n
    n+=1
    print('%12d%12d%12d' % (poly, exp, n))
