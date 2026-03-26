class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def back(i, sum_, path):
            if sum_ == target:
                output.append(path[:])
                return 

            if sum_ > target:
                return 

            for j in range(i, n):

                if j == 0 or candidates[j] != candidates[j-1] or not unvisited[j - 1]:
                # if unvisited[j]:
                    path.append(candidates[j])
                    unvisited[j] = False

                    back(j + 1, sum_ + candidates[j], path)

                    unvisited[j] = True
                    path.pop()

        output = []
        n = len(candidates)
        candidates.sort()

        unvisited = [True] * n
        back(0, 0, [])

        return output
        