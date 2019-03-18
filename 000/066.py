'''
    Plus One
    Runtime: 44 ms
'''

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        
        while i >= 0:
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
            i -= 1
        
        newDig = [0] * (len(digits) + 1)
        newDig[0] = 1
        return newDig