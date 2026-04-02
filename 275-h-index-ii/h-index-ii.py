class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        pos = {citations[i] : i for i in range(n)}
        
        left = 1
        right = citations[-1]

        while right >= left:
            mid = (right + left) // 2

            idx = bisect_left(citations, mid)
            
            if mid <= n - idx:
                left = mid + 1

            else:
                right = mid - 1    

        return right