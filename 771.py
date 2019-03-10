'''
    Jewels and Stones
    Runtime: 56 ms
'''

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        
        jewels = list(J)
        count = 0
        for jewel in jewels:
            if jewel in S:
                count += S.count(jewel)

        return count