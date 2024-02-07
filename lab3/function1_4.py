def isprime(n):
    if n > 1:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
                break
        return True
    else:
        return False

def filter_prime(numbers):
    primes = []
    for num in numbers:
        if isprime(int(num)):
            primes.append(num)
    return primes

numbers = [s for s in input().split()]
filtered_numbers = filter_prime(numbers)
print(" ".join(filtered_numbers))