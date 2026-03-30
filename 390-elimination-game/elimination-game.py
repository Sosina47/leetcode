class Solution:
    def lastRemaining(self, n: int) -> int:

        def solve(start, step, remaining, dxn):
            if remaining == 1:
                return start + 1

            if dxn == 0:
                start += step
            
            else:
                if remaining % 2 == 1:
                    start += step

            dxn = abs(dxn - 1)
            
            return solve(start, step * 2, remaining // 2, dxn)

        return solve(0, 1, n, 0) 