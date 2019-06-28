'''
    Robot Return to Origin
    Runtime: 36 ms
'''

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count("L") == moves.count("R") and moves.count("U") == moves.count("D")