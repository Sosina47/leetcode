class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        counter = {}
        count = 0
        length = len(nums)

        for i in range(length):
            if nums[i] in counter:
                counter[nums[i]].append(i)
            else:
                counter[nums[i]]= [i]

        for val in counter.values():
            for i in range(len(val)):
                for j in range(i + 1, len(val)):
                    if (val[i] * val[j]) % k == 0:
                        count += 1


        return count
