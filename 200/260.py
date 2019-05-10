'''
    Single Number III
    Runtime: 36 ms
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        singles = set()

        for num in nums:
            if num in singles:
                singles.remove(num)
            else:
                singles.add(num)

        return list(singles)