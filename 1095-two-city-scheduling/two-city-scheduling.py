class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x: abs(x[0] - x[1]), reverse = True)
        print(costs)

        cost_a = cost_b = 0
        equal = [0]
        
        count_a = count_b = len(costs) // 2
        for a, b in costs:
            if a == b:
                equal.append(a)

            elif a < b:
                if count_a > 0:
                    cost_a += a 
                    count_a -= 1

                else:
                    cost_b += b
                    count_b -= 1
            
            else:
                if count_b > 0:
                    cost_b += b
                    count_b -= 1
                
                else:
                    cost_a += a
                    count_a -= 1

        return cost_a + cost_b + sum(equal) 