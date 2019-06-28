'''
    Number of Segments in a String
    Runtime: 32 ms
'''

class Solution:
    def countSegments(self, s: str) -> int:
        return(len(s.split()))