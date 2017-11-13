def is_semi_prime(number):
    """
    Check if number consists of two multiplied primes.
    """
    if number > 3:
        p = 2
        while number % p:
            p += 1
        q = number / p
        return is_prime(p) and is_prime(q)
    return False


def is_prime(number):
    """
    Check if number is prime.
    """
    return number > 1 and all(number % d for d in range(2, int(number)))
