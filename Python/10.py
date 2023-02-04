
'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

# copied from my solution to 3
def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    for n in range(3,int(x**0.5)+1,2):
        if x % n == 0:
            return False
    return True

out = [2, *[i for i in range(3, 2000000, 2) if is_prime(i)]]
print(sum(out))
