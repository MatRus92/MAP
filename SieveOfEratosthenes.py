from typing import Generator, List

def sieve_eratosthenes(sieve: List[int] = []) -> List[int]:
    if sieve:
        length = len(sieve)
        sieve.extend([True for _ in range(length)])
    else:
        length = 10
        sieve = [True for _ in range(length * 2)]
        sieve[0], sieve[1] = False, False

    # sieve generation
    for i in range(2, length):
        if sieve[i]:
            for j in range(2 * i, 2 * length, i):
                sieve[j] = False

    return sieve

def primes_gen() -> Generator[int, None, None]:
    primes = sieve_eratosthenes()
    prev = 0
    while True:
        for i in range(prev, len(primes)):
            if primes[i]:
                yield i
        prev = len(primes)
        primes = sieve_eratosthenes(primes)


if __name__ == '__main__':
   gen = primes_gen()
   for _ in range(10):
       print(next(gen))



