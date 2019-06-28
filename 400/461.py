'''
    Hamming Distance
    Runtime: 32 ms
'''

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xBinary = "{:032b}".format(x)
        yBinary = "{:032b}".format(y)
        
        distance = 0
        
        for i in range(len(xBinary)):
            if xBinary[i] != yBinary[i]:
                distance += 1
        return distance