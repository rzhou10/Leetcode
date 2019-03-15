'''
    Max Consecutive Ones
    Runtime: 100 ms
'''

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        current = 0
        
        for i in range(len(nums)):
            if nums[i] == 1:
                current += 1
                count = max(count, current)
            else:
                current = 0
        
        return count