class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if m == 0:
            for i in range(n):
                nums1.insert(i, nums2[i])
                nums1.pop()
            return
        
        for i in range(n):
            nums1.pop()
        
        i, j = 0, 0
        while i < m and j < n:
            if nums1[i] > nums2[j]:
                nums1.insert(i, nums2[j])
                j += 1
                m += 1
            i += 1

        while j < n: 
            nums1.append(nums2[j])
            j += 1



