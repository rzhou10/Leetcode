'''
    Palindrome Number
    Runtime: 248 ms (how is this so slow???)
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        if x < 0:
            return False
        strX = str(x)
        
        return strX == strX[::-1]