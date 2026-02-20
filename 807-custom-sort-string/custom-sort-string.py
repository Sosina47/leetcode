class Solution:
    def customSortString(self, order: str, s: str) -> str:
        occurance = Counter(s)
        s = []

        for c in order:
            if c in occurance:
                s.extend([c] * occurance[c])
                del occurance[c]
            
        for key in occurance:
            s.extend([key] * occurance[key])

        return ''.join(s)