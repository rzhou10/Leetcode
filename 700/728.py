'''
    Self Dividing Numbers
    Runtime: 64 ms
'''

class Solution:
    
    def divideHelper(self, i: int) -> bool:
        nums = list(str(i))
        if "0" in nums:
            return False
        for j in nums:
            if i % int(j) != 0:
                return False
        
        return True
    
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        nums = []
        if right < 10:
            i = left
            for i in range(right):
                nums.append(i + 1)
            return nums
        
        for i in range(left - 1, right):
            if self.divideHelper(i + 1):
                nums.append(i + 1)
        
        return nums