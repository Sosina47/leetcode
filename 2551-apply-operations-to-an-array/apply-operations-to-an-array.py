class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        seen = set()
        for i in range(len(nums)):
            if i == 0:
                if nums[i] == nums[i + 1]:
                    nums[i] *= 2
                    nums[i + 1] = 0

            elif 1 <= i < len(nums) - 1 and i not in seen:
                if nums[i] == nums[i + 1]:
                    nums[i] *= 2
                    nums[i + 1] = 0


        write = read = 0

        print(nums)

        while read < len(nums) and write < len(nums):
            if nums[read] != 0:
                read += 1
                continue

            if nums[write] == 0 or write <= read:
                write += 1
                continue

            nums[read], nums[write] = nums[write], nums[read]
            read += 1
            write = 1

        return nums