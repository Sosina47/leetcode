class Solution:
    def smallestBalancedIndex(self, nums: list[int]) -> int:
        limit = 10 ** 9 * 10 ** 5
        left_sum = list(accumulate(nums))
        left_sum.append(0)

        nums.reverse()
        right_product = [1]
        for i in range(len(nums)):
            right_product.append(min(right_product[-1] * nums[i], limit))

        right_product.reverse()

        for i in range(len(nums)):
            if left_sum[i - 1] == right_product[i + 1]:
                return i

        return -1