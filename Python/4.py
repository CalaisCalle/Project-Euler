'''
A palindromic number reads the same both ways. The largest palindrome made
 from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def pal(low, high):
    for i in range(high, low, -1):
        for j in range(high, low, -1):
            candidate = str(i * j)
            if candidate == candidate[::-1]:
                print(i, j)
                yield int(candidate)

print(max(list(pal(100,999))))