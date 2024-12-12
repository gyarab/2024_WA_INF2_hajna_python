def fibonacci(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer")
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    

def test_fibonacci(n):
    try:
        result = fibonacci(n)
        print(f"Fibonacci({n}) = {result}")
        return result
    except ValueError as e:
        print(e)
        return None

def is_prime(n):
    if not isinstance(n, int) or n < 1:
        raise ValueError("n must be an integer")
    if n == 0:
        return False
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    test_fibonacci(10)
    test_fibonacci(-1)
    test_fibonacci(0)
    test_fibonacci(1)
    test_fibonacci(5)
    try:
        print(is_prime(11))
        print(is_prime(4))
        print(is_prime(1))
        print(is_prime(-1))
        print(is_prime(0.9))
    except ValueError as e:
        print(e)