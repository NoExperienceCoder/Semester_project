from __future__ import division


e_frac = [1, 2, 6, 1, 3, 5, 4, 22, 1, 1, 4]
value = 1.4655712318767680266567312

def display(n, d, exact):
    print (n,'\t' ,d, '\t', n/d, '\t',n/d - exact)

def approx(a, exact):
    # initialize the recurrence
    n0 = a[0]
    d0 = 1
    n1 = a[0]*a[1] + 1
    d1 = a[1]

    display(n0, d0, exact)
    display(n1, d1, exact)

    for x in a[2:]:
        n = x*n1 + n0 # numerator
        d = x*d1 + d0 # denominator
        display(n, d, exact)
        n1, n0 = n, n1
        d1, d0 = d, d1

approx(e_frac, value)