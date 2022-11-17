'''
A palindromic number reads the same both ways. The largest palindrome made
 from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

# how do you create a palindromic number?
three_digits = [i for i in range(100, 1000)]
smallest_mul = three_digits[0]**2
largest_mul = three_digits[-1]**2
# maximum must be less than 888888
# and greater than 10001
dig = 6
def find_pal(digits):
    ...
print(smallest_mul, largest_mul)