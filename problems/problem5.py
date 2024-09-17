def fibonacci(n):
    if n <= 0:
        print("Input should be positive integer.")
    # TODO complete this function
    # so that it returns the nth number in the Fibonacci sequence
    # where n' is always the sum of the two previous numbers
    # e.g. 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 ...
    # so fibonacci(0) = 0, fibonacci(1) = 1, fibonacci(2) = 1, fibonacci(3) = 2, etc.

if __name__ == '__main__':
    for i in range(1, 10):
        print(fibonacci(i))
