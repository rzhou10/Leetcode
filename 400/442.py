'''
    Find All Duplicates in an Array
    Runtime: 148 ms
'''

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dups = set()
        arr = []
        
        for i in nums:
            if i in dups:
                arr.append(i)
            else:
                dups.add(i)

        return arr