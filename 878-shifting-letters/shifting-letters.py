class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        orders = [ord(c) - ord('a') for c in s]
        prefix_diff = [0] * len(s)

        for i in range(len(shifts)):
            prefix_diff[i] += shifts[i]

        diff = 0
        for i in range(len(prefix_diff) - 1, -1, -1):
            diff += prefix_diff[i]
            orders[i] = (orders[i] + diff) % 26
        
        for i in range(len(orders)):
            orders[i] = chr(ord('a') + orders[i])

        return ''.join(orders)