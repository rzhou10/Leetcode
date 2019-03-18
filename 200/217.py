'''
    Contains Duplicate
    Runtime: 44 ms
'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)