'''
    Number Complement
    Runtime: 40 ms
'''

class Solution:
    def findComplement(self, num: int) -> int:
        binary = list(bin(num).lstrip("0b"))
        
        for i in range(len(binary)):
            if binary[i] == "1":
                binary[i] = "0"
            else:
                binary[i] = "1"
        
        return int("".join(binary), 2)