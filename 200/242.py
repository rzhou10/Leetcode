'''
    Valid Anagram
    Runtime: 68 ms
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return ''.join(sorted(s)) == ''.join(sorted(t))