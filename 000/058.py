'''
    Length of Last Word
    Runtime: 24 ms
'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 0:
            return 0
        words = s.split(" ")
        filtered = list(filter(lambda x: len(x) > 0, words))
        
        if len(filtered) == 0:
            return 0
        
        return len(filtered[-1])