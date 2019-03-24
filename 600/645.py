'''
    Set Mismatch
    Runtime: 68 ms
'''

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        allNums = [0] * (len(nums) + 1)
        output = [0, 0]
        
        for i in nums:
            allNums[i] += 1
        
        for i in range(len(allNums)):
            if allNums[i] == 2:
                output[0] = i
            elif allNums[i] == 0:
                output[1] = i
        
        return output