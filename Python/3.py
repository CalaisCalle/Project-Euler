
'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    else:
        return True

def find_factors(val):
    i = 3
    while val != 1:
        if is_prime(i) and val % i == 0:
            yield i
            val /= i
        i+=2

print(max(list(find_factors(600851475143))))
