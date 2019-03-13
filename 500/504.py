'''
    Fibonacci Number
    Runtime: 1680 ms
'''

class Solution:
    def fib(self, N: int) -> int:
        memo = {}
        
        if N < 2:
            return N
        
        if N in memo.keys():
            return memo[N]
        
        diff = self.fib(N - 1) + self.fib(N - 2)
        memo[N] = diff
        
        return diff