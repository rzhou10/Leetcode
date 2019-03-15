'''
    Find the Difference
    Runtime: 56 ms
'''

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sChar = list(s)
        tChar = list(t)
        sChar.sort()
        tChar.sort()
        
        for i, j in zip(sChar, tChar):
            if i != j:
                return j
        
        return tChar[len(tChar) - 1]