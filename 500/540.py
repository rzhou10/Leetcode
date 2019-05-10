'''
    Single Element in a Sorted Array
    Runtime: 36 ms
'''

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        single = set()
        for i in nums:
            if not i in single:
                single.add(i)
            else:
                single.remove(i)
        return single.pop()