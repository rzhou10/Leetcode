'''
    Counting Bits
    Runtime: 160 ms
'''

class Solution:
    def countBits(self, num: int) -> List[int]:
        bits = []
        
        i = 0
        while i <= num:
            binary = list(bin(i))
            bits.append(binary.count("1"))
            i += 1
            
        return bits