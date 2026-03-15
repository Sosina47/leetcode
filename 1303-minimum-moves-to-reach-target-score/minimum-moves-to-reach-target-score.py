class Solution:
    def moves(self, target, double):
        if target == 1 or double == 0:
            return target

        if target % 2 == 1:
            return 2 + self.moves((target - 1) // 2, double - 1)

        else:
            return 1 + self.moves(target // 2, double - 1)


    
    def minMoves(self, target: int, maxDoubles: int) -> int:
        return self.moves(target, maxDoubles) - 1