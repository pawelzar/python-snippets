def is_semi_prime(number):
    """
    Check if number consists of two multiplied primes.
    """
    if number > 3:
        p = 2
        while number % p and p < number:
            p += 1
        q = number / p
        if is_prime(p) and is_prime(q):
            return True
    return False


def is_prime(number):
    """
    Check if number is prime.
    """
    return number > 1 and all(
        number % divisor for divisor in range(2, int(number))
    )
