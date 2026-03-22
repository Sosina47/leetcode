class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_odd = float("inf")

        for i in range(len(nums1)):
            if nums1[i] % 2 == 1:
                min_odd = min(min_odd, nums1[i])

        if min_odd == float("inf"):
            return True

        for i in range(len(nums1)): 
            if nums1[i] % 2 == 0 and nums1[i] < min_odd:
                return False

        return True 