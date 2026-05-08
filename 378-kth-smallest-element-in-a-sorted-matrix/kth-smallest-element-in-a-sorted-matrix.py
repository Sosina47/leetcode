class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        n = len(matrix)

        for r in range(n):
            for c in range(n):
                heappush(heap, -matrix[r][c])

                if len(heap) > k: 
                    heappop(heap)

        return -heap[0]