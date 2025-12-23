class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        length = len(nums)
        for i in range(length):
            if nums[i] < 0:
                neg.append(nums[i])
            else:
                pos.append(nums[i])

        indexP = 0
        indexN = 0
        for i in range(length):
            if i % 2:
                nums[i] = neg[indexN]
                indexN += 1
            else:
                nums[i] = pos[indexP]
                indexP += 1

        return nums