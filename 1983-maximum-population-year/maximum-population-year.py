class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        prefix = [0] * 101
        mod = 1950
        for birth, death in logs:
            prefix[birth % mod] += 1
            prefix[death % mod] -= 1

        prefix = list(accumulate(prefix))
        max_ = max(prefix)
        index = prefix.index(max_)
        return index + mod