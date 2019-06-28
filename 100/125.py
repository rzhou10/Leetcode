'''
    Valid Palindrome
    Runtime: 68 ms
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = list(s.lower())
        
        letters = list(filter(lambda x: x.isalpha() or x.isdigit(), chars))
        print(chars)
        reverseList = letters.copy()
        reverseList.reverse()
        print(reverseList)
        
        return letters == reverseList