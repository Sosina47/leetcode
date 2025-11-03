class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        prev_index = 0
        min_time = 0
        is_doubled = False
        for index in range(1, len(colors)):
            if colors[prev_index] == colors[index]:
                is_doubled = True
                min_time += min(neededTime[prev_index], neededTime[index])
            else:
                is_doubled = False

            if neededTime[prev_index] > neededTime[index] and is_doubled:
                continue
            prev_index = index
        
        return min_time
    