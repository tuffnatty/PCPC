from numba import jit, int64

@jit(int64(int64))
def fibIter(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a
