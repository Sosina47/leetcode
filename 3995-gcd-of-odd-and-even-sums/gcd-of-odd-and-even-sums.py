class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        odd = 0
        even = 0

        for i in range(1, 2 * n + 1): 
            if i % 2: 
                odd += i

            else: 
                even += i

        return math.gcd(odd, even)