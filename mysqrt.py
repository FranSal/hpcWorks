# -*- coding: utf-8 -*-
"""
sqrt using the Newton mwthod

"""

def sqrt2(x):
    s=1
    kmax=100
    delta=1e-14
    for k in range(kmax):
            print "Before iteration %s, s = %20.15f" %(k,s)
            s0=s
            s= 0.5 *(s+x/s)
            if abs(s-s0)/x < delta:
                break
    print ("\nAfter %s iterations, s = %20.15f" %(k+1,s))

