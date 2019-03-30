'''
    Reverse Words in a String
    Runtime: 52 ms
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        allWords = list(filter(lambda x: len(x) > 0, s.split(" ")))
        
        allWords.reverse()
        
        return " ".join(allWords)