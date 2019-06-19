'''
    Find Pivot Index
    Runtime: 52 ms
'''

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        front = 0
        back = 0
        
        for i in range(len(nums)):
            back += nums[i]
        
        for i in range(len(nums)):
            if front == back - front - nums[i]:
                return i
            front += nums[i]

        return -1