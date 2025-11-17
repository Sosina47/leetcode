class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        for i in range(len(nums1)):
            index = nums2.index(nums1[i])
            foundGreater = False
            for j in range(index + 1, len(nums2)):
                if nums1[i] < nums2[j]:
                    nums1[i] = nums2[j]
                    foundGreater = True
                    break
            if not foundGreater:
                nums1[i] = -1


        return nums1