'''
    Duplicate Zeros
    Runtime: 48 ms
'''

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        
        res = []
        for x in arr:
            res.append(x)
            if x == 0:
                res.append(x)
        for i in range(len(arr)):
            arr[i] = res[i]
