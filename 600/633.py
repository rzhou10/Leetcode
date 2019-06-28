'''
    Sum of Square Numbers
    Runtime: 152 ms
'''

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        low = 0
        high = int(math.sqrt(c))
        while low <= high:
            if (low * low) + (high * high) == c:
                return True
            elif (low * low) + (high * high) < c:
                low += 1
            else:
                high -= 1
        return False