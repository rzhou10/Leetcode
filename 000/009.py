'''
    Palindrome Number
    Runtime: 92 ms
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        strX = str(x)
        
        return strX == strX[::-1]