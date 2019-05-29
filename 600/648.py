'''
    Replace Words
    Runtime: 248 ms
'''

class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        words = sentence.split(" ")
        
        for i in range(len(words)):
            for j in dict:
                if words[i][0:len(j)] == j:
                    words[i] = j
                    break
        
        return " ".join(words)