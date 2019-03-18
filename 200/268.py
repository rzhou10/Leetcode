'''
    Missing Number
    Runtime: 52 ms
'''

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        newArr = [0] * (len(nums) + 1)
        
        for i in nums:
            newArr[i] += 1
        
        for i in range(len(newArr)):
            if newArr[i] == 0:
                return i