'''
    Reverse Words in a String III
    Runtime: 44 ms
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s[::-1]
        arr = s.split(" ")
        reverse = arr[::-1]
        return " ".join(reverse)