'''
    Height Checker
    Runtime: 36 ms
'''

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sortedHeight = sorted(heights)
        
        difference = 0
        for i, j in zip(heights, sortedHeight):
            if i != j:
                difference += 1
                
        return difference