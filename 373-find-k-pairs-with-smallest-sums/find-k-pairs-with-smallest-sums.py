class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        seen = set()
        output = []

        heap = []
        heappush(heap, [nums1[0] + nums2[0], 0, 0]) 

        while len(output) < k: 
            _, i, j = heappop(heap)
            output.append([nums1[i], nums2[j]])

            if len(nums1) > i + 1: 
                pair = (i + 1, j)

                if pair not in seen:
                    heappush(heap, [nums1[i + 1] + nums2[j], i + 1, j])
                    seen.add(pair)

            if len(nums2) > j + 1: 
                pair = (i, j + 1)

                if pair not in seen: 
                    heappush(heap, [nums1[i] + nums2[j + 1], i, j + 1])
                    seen.add(pair)

        return output
