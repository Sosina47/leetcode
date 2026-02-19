class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        dict = defaultdict(int)
        left = 0
        count_substrings = 0

        for right in range(len(s)):
            dict[s[right]] += 1

            while len(dict) == 3:
                count_substrings += len(s) - right

                if dict[s[left]] == 1:
                    del dict[s[left]]
                else:
                    dict[s[left]] -= 1

                left += 1

        return count_substrings