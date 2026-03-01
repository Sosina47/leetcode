class Solution:
    def partitionString(self, s: str) -> int:
        cur = set()
        count = 0
        for c in s:
            if c in cur:
                count += 1
                cur = set()

            cur.add(c)

        return count + 1