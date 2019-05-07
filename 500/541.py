'''
    Reverse String II
    Runtime: 44 ms
'''

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        allChars = list(s)
        i = 0
        
        while i < len(allChars):
            left = i
            right = min(i + k - 1, len(allChars) - 1)
            
            while left < right:
                temp = allChars[left]
                allChars[left] = allChars[right]
                allChars[right] = temp
                left += 1
                right -= 1
            i += 2 * k
                
        return "".join(allChars)