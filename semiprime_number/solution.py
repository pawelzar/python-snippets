def is_semiprime(number):
    """Return True if the number consists of two multiplied primes."""
    if number > 3:
        prime = lambda n: all(n % a for a in range(2, int(n)))
        p = 2
        while number % p and p < number:
            p += 1
        q = number / p
        if prime(p) and prime(q):
            return True
    return False
