'''
    Single Number III
    Runtime: 44 ms
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        count = {}
        
        for i in nums:
            if i not in count:
                count[i] = 0
            count[i] += 1

        single = []
        for key, value in count.items():
            if value == 1:
                single.append(key)
        
        return single