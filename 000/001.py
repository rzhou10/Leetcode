'''
    Two Sum
    Runtime: 36 ms
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for index in range(0, len(nums)):
            diff = target - nums[index]
            if diff in lookup:
                return [lookup[diff], index]
            else: 
                lookup[nums[index]] = index