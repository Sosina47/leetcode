class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        min_cost = min(min(basket1), min(basket2))

        basket1 = Counter(basket1)
        basket2 = Counter(basket2)
        to_swap1 = []
        to_swap2 = []

        for key, val in basket1.items():
            if key not in basket2:
                if val % 2 == 1:
                    return -1

                to_swap1.append([key, val // 2])
            
            else:
                diff = val - basket2[key]

                if diff % 2 == 1:
                    return -1
                
                if diff > 0:
                    to_swap1.append([key, diff // 2])
                elif diff < 0:
                    to_swap2.append([key, abs(diff) // 2])

        
        for key, val in basket2.items():
            if key not in basket1:
                if val % 2 == 1:
                    return -1

                to_swap2.append([key, val // 2])

        to_swap1.sort(reverse = True)
        to_swap2.sort()
        cost = 0
        i = j = 0
        n1 = len(to_swap1)
        n2 = len(to_swap2)
        
        while i < n1 and j < n2:
            cur_cost = min(to_swap1[i][0], to_swap2[j][0])
            cost += min(cur_cost, 2 * min_cost)
            to_swap1[i][1] -= 1
            to_swap2[j][1] -= 1

            if to_swap1[i][1] == 0:
                i += 1
            if to_swap2[j][1] == 0:
                j += 1

        return cost
        

            
        