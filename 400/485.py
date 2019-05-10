'''
    Max Consecutive Ones
    Runtime: 72 ms
'''

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxl = l = 0
        for n in nums:
            if n == 1:
                l += 1
            else:
                maxl = max(maxl, l)
                l = 0
        return max(maxl, l)