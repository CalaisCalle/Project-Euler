'''
2520 is the smallest number that can be divided by each of the numbers from 
1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
'''

'''
Thought process
================

First: the prime numbers have to be included in the multiplication

Then: the highest power of each prime is all that needs to be included
as this will contain all necessary multiples of that prime.

The primes can be substituted for their highest powers.
'''
primes = [2, 3, 5, 7, 11, 13, 17, 19]

def get_factors(primes):
    for p in primes:
        i = 2
        while p**i < 20:
            i+=1
        yield(p**(i-1))

def mul_all(factors):
    mul = 1
    for f in factors:
        mul *= f
    return mul

print(mul_all(list(get_factors(primes))))