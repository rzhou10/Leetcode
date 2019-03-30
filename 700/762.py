'''
    Prime Number of Set Bits in Binary Representation
    Runtime: 212 ms
'''

class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        count = 0
        
        primes = [2, 3, 5, 7, 11, 13, 17, 19]
        while L <= R:
            if bin(L).count("1") in primes:
                count += 1
            L += 1
        
        return count