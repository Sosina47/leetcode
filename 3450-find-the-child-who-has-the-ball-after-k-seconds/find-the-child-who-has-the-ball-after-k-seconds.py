class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        if k // (n - 1) % 2:
            return n - 1 - k % (n - 1)
        else:
            return k % (n - 1)
