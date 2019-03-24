'''
    Valid Perfect Square
    Runtime: 36 ms
'''

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        
        low = 0
        high = num / 2 + 1
        
        while low <= high:
            mid = int(low + (high - low) / 2)
            if mid * mid == num:
                return True
            elif mid * mid < num:
                low = mid + 1
            else:
                high = mid - 1
        
        return False