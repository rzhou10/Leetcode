'''
    Reverse Bits
    Runtime: 28 ms
'''

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        binary = format(n, "032b")
        return int(binary[::-1], 2)