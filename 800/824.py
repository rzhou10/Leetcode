'''
    Goat Latin
    Runtime: 32 ms
'''

class Solution:
    def toGoatLatin(self, S: str) -> str:
        slist = S.split()
        
        for i, k in enumerate(slist):
            if k[0].lower() in ("a","e","i","o","u"):
                slist[i] += "ma"
            else:
                slist[i] = slist[i][1:] + slist[i][:1] + "ma"
            
            slist[i] = slist[i] + "a"*(i+1)
        
        return " ".join(slist)