def fq(x):
    y = -5 + x + x**2
    return y

def bisection(a, b, TOL):
    fa = fq(a)

    while abs(a - b) > TOL:
        c = (a + b) / 2
        fc = fq(c)

        if fc == 0:
            return c
        elif fc * fa > 0:
            a = c
            fa = fc
        else:
            b = c

    return (a + b) / 2

## Don't edit below this line.
## ====================================================

if __name__ == '__main__':
    xa = float(input('a:'))
    xb = float(input('b:'))
    tol = float(input('TOL:'))

    root = bisection(xa, xb, tol)
    print("f({:,.3f})={:,.5f}".format(root, fq(root)))