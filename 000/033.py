'''
    Search in Rotated Sorted Array
    Runtime: 32 ms
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        
        return -1