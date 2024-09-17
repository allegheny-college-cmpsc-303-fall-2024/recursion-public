def gcd_subtract(a, b):
    if a == b:
        return a
    # TODO complete this function so that
    # it returns the greatest common divisor of a and b
    # it will be called by gcd_swap, which will ensure that a >= b
    raise NotImplementedError

def gcd_swap(a, b):
    if a < b:
        return gcd_subtract(b, a)
    else:
        return gcd_subtract(a, b)

if __name__ == '__main__':
    print(gcd_swap(10, 24))
