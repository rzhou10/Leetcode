'''
    Detect Capital
    Runtime: 40 ms
'''

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        return word.isupper() or word.islower() or word.istitle()