'''
    Unique Morse Code Words
    Runtime: 56 ms
'''

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        code = []
        for i in words:
            temp = ""
            for j in i:
                index = ord(j) - 97
                temp += morse[index]
            code.append(temp)
        
        return len(set(code))