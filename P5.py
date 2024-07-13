def numsys(n):
    return bin(n), hex(n)

if __name__ == '__main__':
    results = numsys(20)
    print('results = {}'.format(results))
    
    b = bin(30)
    h = hex(30)
    print('b = {}'.format(b))
    print('h = {}'.format(h))

    print(numsys(10))
    print(numsys(20))
