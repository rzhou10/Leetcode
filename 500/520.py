'''
    Detect Capital
    Runtime: 60 ms
'''

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        count = 0
        for i in word:
            if ord(i) > 64 and ord(i) < 91:
                count += 1
        
        return count == len(word) or count == 0 or (count == 1 and (ord(word[0]) > 64 and ord(word[0]) < 91))