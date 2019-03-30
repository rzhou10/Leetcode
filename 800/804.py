'''
    Unique Morse Code Words
    Runtime: 36 ms
'''

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        code = set()
        for i in words:
            temp = ""
            for j in i:
                index = ord(j) - 97
                temp += morse[index]
            code.add(temp)
        
        return len(code)