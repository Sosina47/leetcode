class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights) 
        heap = []

        for i in range(n - 1):
            x = heights[i]
            y = heights[i + 1]

            if x >= y:
                continue

            d = y - x
            
            if ladders > 0:
                heappush(heap, d)
                ladders -= 1
                continue

            if heap and d > heap[0]:
                if bricks < heap[0]:
                    return i

                d = heapreplace(heap, d)

            if bricks < d:
                return i

            bricks -= d
        
        return n - 1
            