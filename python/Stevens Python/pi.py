#!/usr/bin/env python
from __future__ import with_statement
import decimal

percision = 1000


def pi_gauss_legendre():
    D = decimal.Decimal
    with decimal.localcontext() as ctx:
        ctx.prec += 2                
        pi_fun = lambda a,b,t: (a + b)**2 / (4 * t)                
        a, b, t, p = 1, 1/D(2).sqrt(), 1/D(4), 1                
        pi, piold = pi_fun(a, b, t), None
        while pi != piold:
            piold = pi
            an = (a + b) / 2
            b = (a * b).sqrt()
            t -= p * (a - an)**2
            a, p = an, 2*p
            pi = pi_fun(a, b, t)                
    return +pi


decimal.getcontext().prec = percision
print pi_gauss_legendre()
