'''
    Peak Index in a Mountain Array
    Runtime: 36 ms
'''

class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        return A.index(max(A))