class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        n = len(matchsticks)
        matchsticks.sort(reverse = True)
        sticks = [0, 0, 0, 0]

        summ = sum(matchsticks)
        if summ % 4 != 0:
            return False
        
        side = summ // 4
        
        def solve(index, sticks):            
            if index == n:
                if max(sticks) == min(sticks) and sticks[0] > 0:
                    return True

                return False

            for i in range(4):
                if i > 0 and sticks[i] == sticks[i - 1]:
                    continue

                if sticks[i] + matchsticks[index] <= side:
                    sticks[i] += matchsticks[index]

                    if solve(index + 1, sticks):
                        return True

                    sticks[i] -= matchsticks[index]

                    if sticks[i] == 0:
                        break

            return False

        return solve(0, sticks)


                    