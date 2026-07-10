class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = ''
        for c in str(n):
            if c != '0': 
                x += c

        x = int(x) if x else 0

        summ = 0
        for i in str(x):
            summ += int(i)

        return x * summ