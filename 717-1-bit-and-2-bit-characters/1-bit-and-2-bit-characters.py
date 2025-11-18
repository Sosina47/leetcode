class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        length = len(bits)
        if length == 1:
            return True
        if bits[-2] == 0:
            return True
        
        last_elements = None

        i = 0
        while i < length - 1:
            if bits[i] == 1:
                last_elements = [i, i + 1]
                i += 2
            else:
                i += 1
            print(last_elements)
            if last_elements == [length - 2,  length - 1]:
                return False
            
        return True
