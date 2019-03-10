'''
    To Lower Case
    Runtime: 44 ms
'''

class Solution:
    def toLowerCase(self, str: str) -> str:
        lower = ""
        
        for i in str:
            if ord(i) < 97 and ord(i) > 64:
                lower += chr(ord(i) + 32)
            else:
                lower += i
                
        return lower