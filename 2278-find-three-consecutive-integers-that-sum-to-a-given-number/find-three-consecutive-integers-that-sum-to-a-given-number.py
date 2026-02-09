class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        n = num // 3

        if n - 1 + n + n + 1 == num:
            return [n-1, n, n + 1]
        return []