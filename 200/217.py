'''
    Contains Duplicate
    Runtime: 56 ms
'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for i in nums:
            if i not in count:
                count[i] = 0
            count[i] += 1
        
        for key, value in count.items():
            if value >= 2:
                return True
        
        return False