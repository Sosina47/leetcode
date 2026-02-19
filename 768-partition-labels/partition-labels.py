class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        frequency = Counter(s)
        start = 0
        output = []

        visiting = {}
        for i in range(len(s)):
            if s[i] in visiting:

                if visiting[s[i]] == 1:
                    del visiting[s[i]]

                else:
                    visiting[s[i]] -= 1

            else:
                if frequency[s[i]] > 1:
                    visiting[s[i]] = frequency[s[i]] - 1

            if not visiting:
                output.append(i - start + 1)
                start = i + 1
        
        return output