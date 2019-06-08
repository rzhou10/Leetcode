'''
    Keyboard Row
    Runtime: 36 ms
'''

class Solution:
    
    def findChar(self, word: str, row: List[str]) -> bool:
        for i in word:
            if i not in row:
                return False
            
        return True
    
    def findWords(self, words: List[str]) -> List[str]:
        word = []
        arr = ["qwertyuiopQWERTYUIOP", "asdfghjklASDFGHJKL", "zxcvbnmZXCVBNM"]
        
        for i in words:
            if i[0] in arr[0]:
                if self.findChar(i[1:], arr[0]):
                    word.append(i)
            elif i[0] in arr[1]:
                if self.findChar(i[1:], arr[1]):
                    word.append(i)
            elif i[0] in arr[2]:
                if self.findChar(i[1:], arr[2]):
                    word.append(i)
                
        return word