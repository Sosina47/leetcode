class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def back(i, path):
            if i > n:
                return 

            output.append(path[:])

            for j in range(i, n):
                path.append(nums[j])

                back(j + 1, path)
                
                path.pop()

        output = []
        n = len(nums)

        back(0, [])

        return output