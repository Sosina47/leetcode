class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        max_weight = sum(weights)
        min_weight = max(weights)

        # print(max_weight, min_weight)

        def countDays(weight):
            count = 0            
            cur_weight = 0

            for w in weights:
                if cur_weight + w > weight:
                    count += 1
                    cur_weight = 0
                
                cur_weight += w
            
            return count + 1
            

        left = min_weight
        right = max_weight

        while right >= left:
            mid = (right + left) // 2

            if countDays(mid) > days:
                left = mid + 1

            else:
                right = mid - 1

        return left