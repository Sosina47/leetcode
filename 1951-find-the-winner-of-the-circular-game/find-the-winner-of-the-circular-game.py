class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        nums = [i for i in range(1, n + 1)]
        
        def solve(index, players):
            if len(players) == 1:
                return players[0]

            loser = (index + k - 1) % len(players)
            next = loser % (len(players) - 1)

            players = players[:loser] + players[loser + 1 :]

            return solve(next, players)

        return solve(0, nums)