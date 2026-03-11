class Solution:
    def decodeString(self, s: str) -> str:
        nums = []
        chars = []

        num = 0
        cur = ''

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)

            elif c == '[':
                nums.append(num)
                chars.append(cur)
                cur = ''
                num = 0

            elif c == ']':
                cur = chars.pop() + cur * nums.pop()

            else:
                cur += c

        return cur