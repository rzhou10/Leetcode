'''
    Peak Index in a Mountain Array
    Runtime: 60 ms
'''

class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        index = 0
        maxN = 0
        for i in range(len(A)):
            if A[i] > maxN:
                maxN = A[i]
                index = i
        
        return index