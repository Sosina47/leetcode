class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pref_sum = []
        for index in range(len(nums)):
            if index == 0:
                pref_sum.append(nums[index])
            else:
                pref_sum.append(nums[index] + pref_sum[index - 1])

        count_subarrays = 0
        freq = {0: 1} 

        for i in range(len(pref_sum)):
            if pref_sum[i] % k in freq:
                count_subarrays += freq[pref_sum[i] % k]
            freq[pref_sum[i] % k] = freq.get(pref_sum[i] % k, 0) + 1

        return count_subarrays