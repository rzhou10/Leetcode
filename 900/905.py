'''
    Sort Array By Parity
    Runtime: 84 ms
'''

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        evens = []
        odds = []
        
        for i in A:
            if i % 2 == 0:
                evens.append(i)
            else:
                odds.append(i)
                
        evens.extend(odds)
        return evens