'''
    Maximum Gap
    Runtime: 48 ms
'''

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        nums.sort()
        
        maxDiff = 0
        
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] > maxDiff:
                maxDiff = nums[i + 1] - nums[i]
                
        return maxDiff