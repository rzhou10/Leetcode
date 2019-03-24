'''
    Find the Duplicate Number
    Runtime: 40 ms
'''

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dups = set()
        
        for i in nums:
            if i in dups:
                return i
            dups.add(i)