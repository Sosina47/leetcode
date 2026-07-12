class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        a = arr[::]
        a = list(set(a))

        a.sort()
        pos = {a[i] : i + 1 for i in range(len(a))} 

        arr = [pos[arr[i]] for i in range(len(arr))]
        return arr