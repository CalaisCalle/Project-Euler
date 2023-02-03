'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

def is_prime(value):
    if value == 1:
        return False
    if value % 2 == 0:
        return False
    for i in range(3, int(value**0.5) + 1, 2):
        if value % i == 0:
            return False
    return True

def generate_primes(n):
    prime_count = 2
    candidate = 5
    latest_prime = 3
    while prime_count < n:
        if is_prime(candidate):
            latest_prime = candidate
            prime_count += 1
        candidate += 2
    
    return latest_prime

print(generate_primes(10001))
