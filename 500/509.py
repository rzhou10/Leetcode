'''
    Fibonacci Number
    Runtime: 32 ms
'''

class Solution:
    memo = {}
    def fib(self, N: int) -> int:
        
        if N < 2:
            return N
        
        if N in self.memo:
            return self.memo[N]
        
        diff = self.fib(N - 1) + self.fib(N - 2)
        self.memo[N] = diff
        
        return diff