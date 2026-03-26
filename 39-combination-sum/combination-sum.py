class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def back(i, sum_, path):
            if sum_ == target:
                output.append(path[:])
                return 

            if sum_ > target:
                return 
            
            # print(path)
            for j in range(i, length):
                path.append(candidates[j])

                back(j, sum_ + candidates[j], path)

                path.pop()

        output = []
        length = len(candidates)
        back(0, 0, [])

        return output