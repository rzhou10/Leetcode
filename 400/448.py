'''
    Find All Numbers Disappeared in an Array
    Runtime: 168 ms
'''

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        allNums = [0] * (len(nums) + 1)
        missing = []
        
        for i in nums:
            allNums[i] += 1
        
        for i in range(len(allNums)):
            if allNums[i] == 0 and i != 0:
                missing.append(i)
                
        return missing