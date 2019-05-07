'''
    Remove Duplicates from Sorted Array
    Runtime: 76 ms
'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)
        
        count = 0
        temp = nums
        for i in range(len(nums) - 1):
            if nums[i] != nums[i + 1]:  
                nums[count] = nums[i] 
                count += 1
        
        nums[count] = nums[len(nums) - 1]
        count += 1
        
            
        return count