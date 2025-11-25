class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = right = 0
        substring = {}
        max_length = 0


        while right < len(s):
            substring[s[right]] = substring.get(s[right], 0) + 1

            while (right - left + 1) - max(substring.values()) > k:
                if substring[s[left]] == 1:
                    substring.pop(s[left])
                else:
                    substring[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)
            right += 1

        return max_length 
        