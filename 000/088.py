'''
    Merge Sorted Array
    Runtime: 36 ms
'''

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index = 0
        i = m
        while i < len(nums1):
            nums1[i] = nums2[index]
            i += 1
            index += 1
        
        nums1.sort()