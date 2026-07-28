class Solution:
    def smallestPalindrome(self, s: str) -> str:
        hash = Counter(s)
        h = sorted(hash)
        mid = ''

        s = []
        for key in h: 
            if not mid and hash[key] % 2 == 1: 
                mid = key
            
            for _ in range(hash[key] // 2):
                s.append(key)
        
        return ''.join(s) + mid + ''.join(s[::-1])