import operator as op
from functools import reduce

def nCr(n, r):
    '''n choose r

        Parameters
        ----------
            n: int
            r: int

        Returns
        -------
            float
    '''

    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom

def atleast(n, t):
    '''gets to probability that your roll at lest n of a die out of t dice

        Parameters
        ----------
            n: int (minimum needed)
            t: int (total number of dice)

        Returns
        -------
            float (the change your roll at lest n of a die out of t)
    '''

    prob = 0
    for k in range(n,t + 1):
        prob += nCr(t, k) * (1/6)**k * (5/6)**(t-k)
    return prob
