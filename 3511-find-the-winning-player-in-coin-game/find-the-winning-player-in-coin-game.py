class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        # if y//4 is even, it means there won't be more coins for alice after bob went his turn
        # if x is also even, there is a chance alice can lose

        possible_moves = min(x, y//4)
        if possible_moves % 2 == 0:
            return 'Bob'
        return 'Alice'