class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        heap = []
        
        for i in range(n - 1):
            if heights[i] >= heights[i + 1]: 
                continue

            d = heights[i + 1] - heights[i]

            if ladders > 0: 
                heappush(heap, d)
                ladders -= 1
                continue
            
            if heap and heap[0] < d: 
                if bricks < heap[0]: 
                    return i

                bricks -= heappop(heap)
                heappush(heap, d)
                continue

            if bricks < d: 
                return i

            bricks -= d

        return n - 1
