'''
    Find First and Last Position of Element in Sorted Array
    Runtime: 48 ms
'''

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        indexes = [-1, -1]
        
        for i in range(len(nums)):
            if nums[i] == target:
                indexes[1] = i
                
        for i, e in reversed(list(enumerate(nums))):
            if nums[i] == target:
                indexes[0] = i
        
        return indexes