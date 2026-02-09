class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_s = Counter(s)
        count_t = Counter(t)

        for key in count_s:
            if key in count_t:
                if count_s[key] >= count_t[key]:
                    count_s[key] -= count_t[key]
                else:
                    count_s[key] = 0
                
        count = 0
        for key in count_s:
            count += count_s[key]

        return count