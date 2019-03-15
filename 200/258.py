'''
    Add Digits
    Runtime: 60 ms
'''

class Solution:
    def addDigits(self, num: int) -> int:
        single = list(str(num))
        
        sumNum = 0
        
        while True:            
            for i in single:
                sumNum += int(i)

            if sumNum < 10:
                return sumNum
            single = list(str(sumNum))
            sumNum = 0
        