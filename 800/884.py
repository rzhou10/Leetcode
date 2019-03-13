'''
    Uncommon Words from Two Sentences
    Runtime: 44 ms
'''

class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        Awords = A.split(" ")
        Bwords = B.split(" ")
        
        uncommon = []
        
        for i in Bwords:
            if i not in Awords and Bwords.count(i) == 1:
                uncommon.append(i)
        
        for i in Awords:
            if i not in Bwords and Awords.count(i) == 1:
                uncommon.append(i)
            
        return uncommon