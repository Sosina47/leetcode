class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if 9 * num < sum: 
            return ""

        res = ''
        while len(res) < num or sum > 0: 
            mn = min(9, sum)
            res += str(mn)

            sum -= mn 

        return res