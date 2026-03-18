class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if k == 0:
            if nums1 == nums2:
                return 0
            return -1

        add = sub = 0
        for i in range(len(nums1)):
            diff = nums1[i] - nums2[i]

            if diff % k != 0: 
                return -1

            if diff > 0:
                sub += diff // k
            else:
                add += abs(diff) // k
            
        if add != sub:
            return -1

        return add