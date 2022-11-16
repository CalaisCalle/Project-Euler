
'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

def is_prime(n):
    if n == 1 or n == 2:
        return True
    if n % 2 == 0:
        return False
    tests = [i for i in range(3, int(n**0.5), 2)]
    for t in tests:
        if n % t == 0:
            return False
    else:
        return True

val = 600851475143
val_sqrt = int(600851475143 ** 0.5)

candidates = [a for a in range(1, val, 2) if val_sqrt % a == 0]
primes = [c for c in candidates if is_prime(c)]

print(primes)