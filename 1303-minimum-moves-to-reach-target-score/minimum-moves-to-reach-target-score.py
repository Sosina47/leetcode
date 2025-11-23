class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count_moves = 0
        while target > 1:
            if target % 2 == 0 and maxDoubles > 0:
                target //= 2
                maxDoubles -= 1
            else:
                if maxDoubles == 0:
                    count_moves =count_moves + target - 1
                    break
                target -= 1
            count_moves += 1
        return count_moves
        