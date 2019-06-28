'''
    Find Smallest Letter Greater Than Target
    Runtime: 36 ms
'''

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for i in letters:
            if ord(i) > ord(target):
                return i
        
        return letters[0]