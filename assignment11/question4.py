def count_primes(n):
    if n < 2:
        return 0
    
    is_prime = [True] * (n + 1)
    is_prime[0], is_prime[1] = False, False  # 0 and 1 are not prime numbers
    
    p = 2
    while p * p <= n:
        # If is_prime[p] is not changed, then it is a prime
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    
    # Count all prime numbers
    return sum(is_prime)

# taking input
n = int(input("Enter a number: "))
print(f"The number of prime numbers from 1 to {n} is {count_primes(n)}")