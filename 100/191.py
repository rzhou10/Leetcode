'''
    Number of 1 Bits
    Runtime: 36 ms
'''

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count("1")