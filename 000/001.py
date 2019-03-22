'''
    Two Sum
    Runtime: 780 ms
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        while True:
            otherTarget = target - nums[i]
            if otherTarget in nums and nums.index(otherTarget) != i:
                return [i, nums.index(otherTarget)]
            i += 1