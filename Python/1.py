'''
Project Euler, Problem 1:

If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. 
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''

sum_mul = lambda a, b: sum([i for i in range(1, 1000) if (i%a==0) or (i%b)==0])

print(sum_mul(3, 5))
