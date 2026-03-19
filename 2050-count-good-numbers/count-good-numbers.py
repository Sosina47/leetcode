class Solution:
    def pow(self, num, n):
        mod = 10 ** 9 + 7
    
        if n == 0:
            return 1

        res = self.pow(num, n // 2)
        
        if n % 2 == 0:
            return (res * res) % mod
        
        return (res * res * num) % mod

    def countGoodNumbers(self, n: int) -> int:
        mod = 10 ** 9 + 7
        odd = n // 2
        even = n - odd

        return self.pow(5, even) % mod * self.pow(4, odd) % mod
