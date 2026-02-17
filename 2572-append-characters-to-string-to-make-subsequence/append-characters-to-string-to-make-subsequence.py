class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        idx_s = idx_t = 0
        while idx_t < len(t):
            if idx_s >= len(s):
                break

            if t[idx_t] == s[idx_s]:
                idx_t += 1

            idx_s += 1

        else:
            return 0

        return len(t) - idx_t