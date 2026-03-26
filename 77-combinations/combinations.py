class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def back(i, path):
            if len(path) == k:
                output.append(path[:])
                return 

            for j in range(i, n + 1):
                path.append(j)

                back(j + 1, path)

                path.pop()

        output = []
        back(1, [])

        return output
