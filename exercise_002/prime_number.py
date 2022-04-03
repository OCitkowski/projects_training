# Define a function that takes one integer argument and returns logical value true or false depending
# on if the integer is a prime.
#
# Per Wikipedia, a prime number (or a prime) is a natural number greater than 1 that has no positive divisors other
# than 1 and itself.
# Requirements
#
#     You can assume you will be given an integer input.
#     You can not assume that the integer will be only positive. You may be given negative numbers as well (or 0).
#     NOTE on performance: There are no fancy optimizations required, but still the most trivial solutions might time
# out. Numbers go up to 2^31 (or similar, depends on language version). Looping all the way up to n, or n/2,
# will be too slow.
#
# Example
#
# is_prime(1)  /* false */
# is_prime(2)  /* true  */
# is_prime(-1) /* false */


# print(
#     f'*{divisors_not2_not3}\n**{divisors_not2_not3_not5}\n***{divisors_not2_not3_not5_not7}\n****{divisors_not2_not3_not5_not7_not11}')
# print(f' {divisors_not2} \n {divisors_not3} \n {divisors_not5} \n {divisors_not7} \n {divisors_not11}')
# divisors = [i for i in divisors_not2_not3_not5_not7_not11 if num % i == 0]
from math import sqrt

def is_prime(num):
    if num in [2, 3, 5, 7, 11]:
        return True
    if num < 2 or num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0 or num % 11 == 0:
        return False
    if sqrt(num) - int(sqrt(num)) == 0:
        return False
    sqrt_num = int(sqrt(num))

    divisors_not2 = [i for i in range(3, sqrt_num, 2) if i < sqrt_num]
    divisors_not3 = [i for i in range(0, sqrt_num, 3) if i < sqrt_num]
    divisors_not5 = [i for i in range(0, sqrt_num, 5) if i < sqrt_num]
    divisors_not7 = [i for i in range(0, sqrt_num, 7) if i < sqrt_num]
    divisors_not11 = [i for i in range(0, sqrt_num, 11) if i < sqrt_num]

    divisors_not2_not3_not5_not7_not11 = sorted(
        list(set(divisors_not2) - set(divisors_not3) - set(divisors_not5) - set(divisors_not7) - set(divisors_not11)))

    for i in divisors_not2_not3_not5_not7_not11:
        if num % i == 0:
            print(i)
            return False
    return True
    divisors = [i for i in range(1, num) if pow(i, 2) < num and num % i == 0]
    return divisors


# Best practic
def is_prime_best_pr(n): return all(n % p for p in [2] + list(range(3, int(n ** .5) + 1))) if n > 2 else n == 2


if __name__ == "__main__":
    # assert is_prime(111) == False
    # assert is_prime(4) == False
    # assert is_prime(5099) == True
    # assert is_prime(11111111111111111111111111111111111) == True
