

def get_primes(n: int):
    primes = [2]
    sieve = [False if i%2==0 else True for i in range(n)]
    for i in range(3, n, 2):
        if sieve[i]:
            primes.append(i)
            for j in range(i*i, n, i):
                sieve[j] = False
    return primes

print(get_primes(10**8))