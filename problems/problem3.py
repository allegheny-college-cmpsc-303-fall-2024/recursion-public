def is_even(n):
    if n == 0:
        return True
    else:
        return is_odd(n - 1)

def is_odd(n):
    # TODO complete this function
    # so that both is_even and is_odd 
    # correctly return True or False

    # hint: they pass the ball to each other!
    # note this recursion structure, as we will
    # see it in next week's lecture
    # on adversarial search

    raise_not_implemented_error()

if __name__ == '__main__':
    print(is_even(9))
    print(is_even(10))
