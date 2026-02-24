class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        occurance = Counter(s)
        current = set()
        prev = 0
        output = []

        for i in range(len(s)):
            if occurance[s[i]] > 1:
                occurance[s[i]] -= 1
                current.add(s[i])

            else:
                if s[i] in current:
                    current.remove(s[i])

                if not current:
                    output.append(i + 1 - prev)
                    prev = i + 1
                    
        return output