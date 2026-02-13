class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map = {}
        seen = set()
        s = list(s.split())

        i = j = 0
        while i < len(pattern) and j < len(s):
            if pattern[i] not in map:
                if s[j] in seen:
                    return False

                map[pattern[i]] = s[j]
                seen.add(s[j])

            else:
                if map[pattern[i]] != s[j]:
                    return False

            i += 1
            j += 1

        if i < len(pattern) or j < len(s):
            return False

        return True