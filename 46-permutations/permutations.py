class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def back(path):
            if len(path) == length:
                output.append(path[:])
                return 

            for i in range(length):
                if not visited[i]:
                    print(nums[i], visited[i])

                    visited[i] = True
                    path.append(nums[i])

                    back(path)

                    visited[i] = False
                    path.pop()
                


        length = len(nums)
        visited = [False] * length

        output = []
        back([])

        return output
