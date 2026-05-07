class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-piles[i] for i in range(len(piles))]

        heapify(piles)

        for _ in range(k):
            n = -heappop(piles)
            n -= n // 2

            heappush(piles, -n)

        return -sum(piles)
