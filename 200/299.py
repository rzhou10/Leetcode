'''
    Bulls and Cows
    Runtime: 84 ms
'''

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        numbers = [0] * 10
        
        for i in range(len(secret)):
            if int(secret[i]) == int(guess[i]):
                bulls += 1
            else:
                if numbers[int(secret[i])] < 0:
                    cows += 1
                if numbers[int(guess[i])] > 0:
                    cows += 1
                numbers[int(secret[i])] += 1
                numbers[int(guess[i])] -= 1
                
        return str(bulls) + "A" + str(cows) + "B"