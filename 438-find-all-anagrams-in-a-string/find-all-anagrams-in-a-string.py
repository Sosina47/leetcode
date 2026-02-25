class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        
        
        c = Counter(p)
        seen = defaultdict(int)
        for i in range(len(p)):
            seen[s[i]] += 1 

        output = []
        if seen == c:
            output.append(0)
        
        left = 0
        for right in range(len(p), len(s)):
            seen[s[right]] += 1
            if seen[s[left]] == 1:
                del seen[s[left]]
            else:
                seen[s[left]] -= 1
            left += 1

            if seen == c:
                output.append(left)

        return output