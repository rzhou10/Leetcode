'''
    Number of Lines To Write String
    Runtime: 48 ms
'''

class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        arr = [0] * 2
        
        for i in range(len(S)):
            arr[1] += widths[ord(S[i]) - ord('a')]
            if arr[1] > 100:
                arr[0] += 1
                arr[1] = widths[ord(S[i]) - ord('a')]
                
        arr[0] += 1
        return arr