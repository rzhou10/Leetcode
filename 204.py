'''
    Count Primes
    Runtime: 676 ms
'''

class Solution:
    def countPrimes(self, n: int) -> int:
        isPrime = [True] * (n + 1)
        
        i = 4
        while i <= n:
            isPrime[i] = False
            i += 2
        
        m = 3
        while m <= n:
            if isPrime[m]:
                j = m * m
                while j < n:
                    isPrime[j] = False
                    j += 2 * m
            m += 2
        
        count = 0
        
        k = 2
        while k < n:
            if isPrime[k]:
                count += 1
            k += 1
        
        return count