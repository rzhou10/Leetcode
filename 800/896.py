'''
    Peak Index in a Mountain Array
    Runtime: 84 ms
'''

class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        
        return all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or all(A[i] >= A[i + 1] for i in range(len(A) - 1))