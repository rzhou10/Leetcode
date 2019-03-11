'''
    N-Repeated Element in Size 2N Array
    Runtime: 76 ms
'''

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        unique = len(set(A)) - 1
        counts = {}
        
        for i in A:
            if i not in counts:
                counts[i] = 0
            counts[i] += 1
        
        element = 0
        
        for key, value in counts.items():
            if value == unique:
                element = key
                break
                
        return element