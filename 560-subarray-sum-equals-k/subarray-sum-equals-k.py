class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        freq = {0: 1}
        pref = [0] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                pref[i] = nums[i]
            else:
                pref[i] = nums[i] + pref[i - 1]
            
            if pref[i] - k in freq:
                count += freq[pref[i] - k]

            freq[pref[i]] = freq.get(pref[i], 0) + 1

        return count
        

    