'''
    Single Element in a Sorted Array
    Runtime: 40 ms
'''

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        count = {}
        
        for i in nums:
            if i not in count:
                count[i] = 0
            count[i] += 1

        dups = []
        for key, value in count.items():
            if value == 1:
                return key