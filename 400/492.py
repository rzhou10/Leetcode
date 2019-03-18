'''
    Construct the Rectangle
    Runtime: 40 ms
'''

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        dim = [0, 0]
        sqd = int(area ** 0.5)
        
        i = 1
        while sqd >= i:
            if area % sqd == 0:
                dim[0] = int(area / sqd)
                dim[i] = sqd
                break
            sqd -= 1
        
        return dim