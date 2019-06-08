'''
    Available Captures for Rook
    Runtime: 36 ms
'''

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        xPoint = 0
        yPoint = 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "R":
                    xPoint = i
                    yPoint = j
                    break
        
        pawns = 0

        # up
        for i in range(yPoint, -1, -1):
            if board[xPoint][i] == "B":
                break
            elif board[xPoint][i] == "p":
                pawns += 1
                break

        # down
        for i in range(yPoint, len(board)):
            if board[xPoint][i] == "B":
                break
            elif board[xPoint][i] == "p":
                pawns += 1
                break

        # left
        for i in range(xPoint, -1, -1):
            if board[i][yPoint] == "B":
                break
            elif board[i][yPoint] == "p":
                pawns += 1
                break

        # right
        for i in range(xPoint, len(board[xPoint])):
            if board[i][yPoint] == "B":
                break
            elif board[i][yPoint] == "p":
                pawns += 1
                break

        return pawns