'''
    Majority Element II
    Runtime: 36 ms
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        for i in nums:
            if i not in count:
                count[i] = 0
            count[i] += 1
        
        allNums = []
        for key, value in count.items():
            if value > len(nums) / 3:
                allNums.append(key)
                
        return allNums