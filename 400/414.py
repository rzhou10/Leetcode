'''
    Third Maximum Number
    Runtime: 56 ms
'''

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        unique = list(set(nums))
        if len(unique) < 3:
            return max(unique)
        maxNo = max(unique)
        unique.remove(maxNo)
        maxNo = max(unique)
        unique.remove(maxNo)
        return max(unique)