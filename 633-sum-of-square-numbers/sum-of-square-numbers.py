class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        for i in range(46341):
            n = c - (i ** 2)
            if n < 0:
                return False

            if n == math.floor(math.sqrt(n)) ** 2:
                return True

        return False 