class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        operations = 0
        limit = nums[-1]

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < limit:
                limit = nums[i]

            elif nums[i] > limit:
                op = nums[i] // limit
                if nums[i] % limit == 0:
                    op -= 1

                operations += op
                pieces = op + 1

                limit = min(limit, nums[i] // pieces)

        return operations