'''
    Repeated String Match
    Runtime: 140 ms
'''

class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        length = math.ceil(len(B) / len(A))
        for i in range(2):
            if B in A * (length + i):
                return length + i
            
        return -1