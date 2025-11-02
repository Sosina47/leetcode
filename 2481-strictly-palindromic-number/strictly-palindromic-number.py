class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for base in range(2, n - 1):
            base_form = ''
            temp = n
            while temp > 0:
                base_form = str(temp % base) + base_form 
                temp //= base
            
            if base_form != base_form[::-1]:
                return False
        
        return True