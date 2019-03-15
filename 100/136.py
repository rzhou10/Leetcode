'''
    Single Number
    Runtime: 48 ms
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = {}
        for i in nums:
            if i not in count:
                count[i] = 0
            count[i] += 1
        
        for key, value in count.items():
            if value == 1:
                return key