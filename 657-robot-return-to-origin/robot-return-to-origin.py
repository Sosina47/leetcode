class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = y = 0

        for c in moves: 
            if c == 'U': 
                y += 1

            elif c == 'D': 
                y -= 1

            elif c == 'R': 
                x += 1

            else: 
                x -= 1

        return x == y == 0