'''
    First Unique Character in a String
    Runtime: 108 ms
'''

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        
        for i in s:
            if i not in count:
                count[i] = 0
            count[i] += 1
            
        for key, value in count.items():
            if value == 1:
                return s.index(key)
        
        return -1