class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = list(map(lambda x: x * -1, stones))

        heapify(stones)
        print(stones)
        
        while len(stones) > 1: 
            x = heappop(stones) * -1
            y = heappop(stones) * -1

            if x > y: 
                heappush(stones, y - x)

        return stones[0] * -1 if stones else 0