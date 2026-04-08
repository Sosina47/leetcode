class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)
        
        def solve(prev, end):
            if end == n:
                return prev != int(s)
            
            for i in range(end, n):
                num = int(s[end : i + 1])

                if num == 0 and i < n - 1:
                    continue

                if prev == -1:
                    if solve(num, i + 1):
                        return True
                
                else:
                    
                    if num >= prev:
                        return False

                    if prev - num == 1:
                        return solve(num, i + 1)

            return False

        return solve(-1, 0) 