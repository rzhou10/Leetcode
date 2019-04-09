'''
    Complement of Base 10 Integer
    Runtime: 36 ms
'''

class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0:
            return 1
        nBin = list(bin(N).lstrip("0b"))
        
        for i in range(len(nBin)):
            if nBin[i] == "1":
                nBin[i] = "0"
            else:
                nBin[i] = "1"
        
        return int("".join(nBin), 2)