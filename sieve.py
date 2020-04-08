class Sieve:
    def __init__(self, n: int, sieve_max=100_000_000):
        self.sieve_max = sieve_max
        self.values = self.sieve(n)

    def sieve(self, n: int) -> [int]:
        """takes n and returns a list of all primes from 2 to n using
        the sieve of Eratosthenes"""
        if n > self.sieve_max:
            raise ValueError(f"{n} exceeds max sieve value ({self.sieve_max}). To override, manually set Sieve's `sieve_max` attribute")
        
        print(f'setting search_max to {n}')
        self.search_max = n

        if n < 2:
            return []
        arr = [True] * (n+1)
        for i in range(2, n+1):
            if arr[i]:
                for j in range(i ** 2, n+1, i):
                    arr[j] = False
        
        return [i for i in range(2,n+1) if arr[i]]
    
    def is_prime(self, n: int) -> bool:
#         print(f'checking if {n} is prime')
        if n < 2:
            return False
        
        if n <= self.search_max:
            return n in self.values
    
        print(f"{n} exceeds search max ({self.search_max})")

        # Re-perform sieve and update self.values
        self.values = self.sieve(n)
        return n in self.values
    
    def prime_factors(self, n: int) -> [int]:
        print(f'looking for factors of {n}')
        
        if n < 2:  # no prime factors
            return []
        
        if n > self.search_max:
            print(f'expanding search max from {self.search_max}...')
            self.values = self.sieve(n)
            print(f'...done')
            
        for prime in self.values:
            if n % prime == 0:
                print(prime)
                return [prime] + self.prime_factors(int(n/prime))

        return []


# Example usage:
# --------------
MAX_VALUE = 1_000

sieve = Sieve(MAX_VALUE)

sieve.search_max  # 1000
sieve.values  # all the primes <= 1000, [2,3,5,...,983,991,997]

sieve.is_prime(999_999)  # False
sieve.values  # all the primes <= 999,999 [2,3,5,...,etc]

pf = sieve.prime_factors(231_510_111)  # ValueError: n exceeds max sieve value

sieve.sieve_max = 250_000_000  # produces about 12.7M primes, might take up to a minute or so.
pf = sieve.prime_factors(231_510_111)  # [3, 7, 23, 479317]

from functools import reduce
reduce(lambda x,y: x*y, pf)  # 231,510,111
