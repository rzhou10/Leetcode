'''
    Rotate String
    Runtime: 36 ms
'''

class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        
        for i in range(len(A)):
            A = A[1:] + A[0]
            if A == B:
                return True
        
        if len(A) == 0 and len(B) == 0:
            return True
        return False