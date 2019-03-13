'''
    Fizz Buzz
    Runtime: 72 ms
'''

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        fB = []
        
        i = 1
        while i <= n:
            if i % 5 == 0 and i % 3 == 0:
                fB.append("FizzBuzz")
            elif i % 3 == 0:
                fB.append("Fizz")
            elif i % 5 == 0:
                fB.append("Buzz")
            else:
                fB.append(str(i))
            i += 1
        
        return fB