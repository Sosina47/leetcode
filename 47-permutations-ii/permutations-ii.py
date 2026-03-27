class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        def back(path):
            if len(path) == length:
                output.append(path[:])
                return 

            for i in range(length):
                if not visited[i] and (i == 0 or nums[i] != nums[i - 1] or visited[i - 1]):

                    visited[i] = True
                    path.append(nums[i])
                    
                    back(path)

                    path.pop()
                    visited[i] = False

        output = []
        length = len(nums)
        nums.sort()

        visited = [False] * length

        back([])
        return output