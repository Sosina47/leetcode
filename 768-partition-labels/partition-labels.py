class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        s_count = Counter(s)
        result = []
        left = 0
        print(s_count)
        chars = set()
        for right in range(len(s)):
            if s_count[s[right]] > 1:
                s_count[s[right]] -= 1
                chars.add(s[right])
            else:
                if s[right] in chars:
                    chars.remove(s[right])
                            
            if not chars:
                result.append(right - left + 1)
                left = right + 1

        return result