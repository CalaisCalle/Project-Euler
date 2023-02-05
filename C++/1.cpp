#include <iostream>

/*
 * Project Euler, Problem 1:
 *
 * If we list all the natural numbers below 10 that are multiples of 3 or 5, 
 * we get 3, 5, 6 and 9. 
 * The sum of these multiples is 23.
 * Find the sum of all the multiples of 3 or 5 below 1000.
*/
int mult_sum(int a, int b, int max = 1000) {
    int ret = 0;
    for (int i = 1; i < max; i++) {
        if (i % a == 0 || i % b == 0) {
            ret += i;
        }
    }
    return ret;
}

int main() {
    std::cout << mult_sum(3, 5) << std::endl;
}