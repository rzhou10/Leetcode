'''
    Next Greater Element I
    Runtime: 44 ms
'''

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextNums = [0] * len(nums1)
        locations = {}
        
        for i in range(len(nums2)):
            locations[nums2[i]] = i
        for i in range(len(nums1)):
            nextNums[i] = -1
            j = locations[nums1[i]]
            
            while j < len(nums2):
                if nums2[j] > nums1[i]:
                    nextNums[i] = nums2[j]
                    break
                j += 1
        
        return nextNums
