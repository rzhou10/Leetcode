'''
    Nim Game
    Runtime: 36 ms
'''

class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0