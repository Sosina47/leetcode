class Solution:
    def largestNumber(self, nums):
        for i in range(1, len(nums)):
            key = nums[i]
            j = i

            while j > 0:
                if str(nums[j]) + str(nums[j - 1]) > str(nums[j - 1]) + str(nums[j]):
                    nums[j], nums[j - 1] = nums[j - 1], nums[j]
                    j -= 1
                else:
                    break

        res = ''.join(map(str, nums))

        return res if res[0] != '0' else '0'