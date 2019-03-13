'''
    Lemonade Change
    Runtime: 48 ms
'''

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bills5 = 0
        bills10 = 0
        
        for i in bills:
            if i == 5:
                bills5 += 1
            elif i == 10:
                if bills5 == 0:
                    return False
                bills5 -= 1
                bills10 += 1
            else:
                if bills5 > 0 and bills10 > 0:
                    bills5 -= 1
                    bills10 -= 1
                elif bills5 >= 3:
                    bills5 -= 3
                else:
                    return False
        
        return True