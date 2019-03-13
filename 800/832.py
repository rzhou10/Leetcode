'''
    Flipping an Image
    Runtime: 48 ms
'''

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for i in A:
            i.reverse()
        
        for i in range(len(A)):
            for j in range(len(A[i])):
                A[i][j] = 1 if A[i][j] == 0 else 0
        
        return A