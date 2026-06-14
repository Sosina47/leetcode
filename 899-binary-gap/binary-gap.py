class Solution:
    def binaryGap(self, n: int) -> int:
        binary = bin(n)[2:]

        gap = 0
        last = -1

        for i in range(len(binary)):
            if binary[i] == '1': 
                if last != -1:
                    gap = max(gap, i - last)

                last = i

        return gap