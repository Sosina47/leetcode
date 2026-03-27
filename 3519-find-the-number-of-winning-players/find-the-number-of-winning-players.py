class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        freq = defaultdict(list)
        count = 0

        for player, picked in pick:
            freq[player].append(picked)

        for key, vals in freq.items():
            vals = Counter(vals)

            if max(vals.values()) > key:
                count += 1

        return count