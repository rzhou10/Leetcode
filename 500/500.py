'''
    Keyboard Row
    Runtime: 48 ms
'''

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        word = []
        arr = ["qwertyuiopQWERTYUIOP", "asdfghjklASDFGHJKL", "zxcvbnmZXCVBNM"]
        
        for i in range(len(words)):
            more = True
            if words[i][0] in arr[0]:
                for j in words[i]:
                    if j not in arr[0]:
                        more = False
                        break
            elif words[i][0] in arr[1]:
                for j in words[i]:
                    if j not in arr[1]:
                        more = False
                        break
            elif words[i][0] in arr[2]:
                for j in words[i]:
                    if j not in arr[2]:
                        more = False
                        break
            
            if more:
                word.append(words[i])
                
        return word