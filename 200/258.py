'''
    Add Digits
    Runtime: 36 ms
'''

class Solution:
    def addDigits(self, num: int) -> int:
        x = 0
        
        while num:
            x += num % 10
            num //= 10
            
        return x if x < 10 else self.addDigits(x)