class Solution:
    def minOperations(self, n: int) -> int:
        if n == 1:
            return 0

        if n % 2 == 0:
            idx1 = n // 2
            idx2 = (n - 1) // 2

            mid = ((2 * idx1) + 1 + (2 * idx2) + 1) // 2
        
        else:
            idx = n // 2
            mid = (2 * idx) + 1

        # it goes till half of the array since when we add 1 in the first half, we are subtracting on one of the element in the other have 
        idx = n // 2 if n % 2 == 0 else (n + 1) // 2 
        operations = 0

        for i in range(idx):
            operations += mid - (2 * i) - 1

        return operations