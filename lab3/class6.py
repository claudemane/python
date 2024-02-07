import math
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n // 2):
        if n % i == 0:
            return False
    return True

numbers = [int(i) for i in input().split()]
prime_numbers = list(filter(lambda x: is_prime(x), numbers))
print(prime_numbers)