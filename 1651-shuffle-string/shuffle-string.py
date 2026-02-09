class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n = len(indices)
        idx = {indices[i]: i for i in range(n)}

        output = [""] * n
        for key in idx:
            output[key] = s[idx[key]]

        return "".join(output)