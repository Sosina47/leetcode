class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        def back(i, sum_, nums):

            if sum_ == n and len(nums) == k:
                output.append(nums[:])
                return 

            if sum_ > n or len(nums) > k:
                return 

            for j in range(i, 10):
                nums.append(j)

                back(j + 1, sum_ + j, nums)

                nums.pop()

        output = []
        back(1, 0, [])

        return output