class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-piles[i] for i in range(len(piles))]

        self.heap_construct(piles)

        for _ in range(k):
            n = -heappop(piles)
            n -= n // 2

            heappush(piles, -n)
            
        return -sum(piles)

    def heap_construct(self, piles):
        n = len(piles)
        
        for i in range(n // 2 - 1, -1, -1):
            cur = i
 
            while True:
                l = 2 * cur + 1
                r = 2 * cur + 2

                smallest = cur

                if l < n and piles[l] < piles[smallest]:
                    smallest = l

                if r < n and piles[r] < piles[smallest]:
                    smallest = r

                if smallest == cur: 
                    break

                piles[cur], piles[smallest] = piles[smallest], piles[cur]
                cur = smallest

        