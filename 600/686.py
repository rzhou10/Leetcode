'''
    Repeated String Match
    Runtime: 280 ms
'''

class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        if A == B or B in A:
            return 1
        
        counter = 0
        repeat = ""
        while len(repeat) < 10000:
            repeat += A
            counter += 1
            if B in repeat:
                return counter
        
        return -1