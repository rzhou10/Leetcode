'''
    Binary Gap
    Runtime: 28 ms
'''

class Solution:
    def binaryGap(self, N: int) -> int:
        maxConsec = 1
        binary = bin(N).lstrip("0b")
        
        if binary.count("1") < 2:
            return 0
        
        current = 1
        for i in binary:
            if i == "1":
                maxConsec = max(maxConsec, current)
                current = 1
            else:
                current += 1
            
        return maxConsec