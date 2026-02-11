class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        x = s1.count('x') + s2.count('x')
        y = s1.count('y') + s2.count('y')

        if x % 2 or y % 2: 
            return -1

        x = y = 0
        for i in range(len(s1)):
            if s1[i] == 'x' and s1[i] != s2[i]:
                x += 1

            elif s1[i] == 'y' and s1[i] != s2[i]: 
                y += 1

        return math.ceil(x / 2) + math.ceil(y / 2)