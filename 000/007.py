'''
    Reverse Integer
    Runtime: 32 ms
'''

class Solution:
    def reverse(self, x: int) -> int:
        temp = x
        if x < 0:
            x = str(x)
            x = x[1:][::-1]
        else:
            x = str(x)
            x = x[::-1]
            
        if(abs(int(x)) > (2 ** 31 - 1)):
            return 0
        if temp < 0:
            x = "-" + x
            return int(x)
        return int(x)