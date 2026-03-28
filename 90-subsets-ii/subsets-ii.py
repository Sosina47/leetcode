class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
         
        def back(i, path):
            output.append(path[:])

            for j in range(i, length):
                if j > 0 and nums[j] == nums[j - 1] and not visited[j - 1]:
                    print(path, j)
                    continue

                path.append(nums[j])
                visited[j] = True

                back(j + 1, path)

                visited[j] = False
                path.pop()
                    

        output = []
        length = len(nums)
        nums.sort()

        visited = [False] * length
        back(0, [])
        
        return output
