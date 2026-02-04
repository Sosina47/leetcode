class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        output = []

        for i in reversed(range(len(arr))):
            if arr.index(i + 1) != i:
                n = arr.index(i + 1) + 1

                if n > 1:
                    self.reverse_arr(n, arr)
                    output.append(n)

                self.reverse_arr(i + 1, arr)
                output.append(i + 1)

        return output
    
    def reverse_arr(self, n, arr):
        reversed_arr = list(reversed(arr[:n]))
        for j in range(n):
            arr[j] = reversed_arr[j]