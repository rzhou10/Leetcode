'''
    Excel Sheet Column Number
    Runtime: 56 ms
'''

class Solution:
    def titleToNumber(self, s: str) -> int:
        result = 0
        
        for i in s:
            result *= 26
            result += ord(i) - ord('A') + 1
        
        return result