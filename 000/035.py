'''
    Search Insert Position
    Runtime: 36 ms
'''

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for x in range(len(nums)):
            if nums[x] >= target:
                return x
            
        return len(nums)