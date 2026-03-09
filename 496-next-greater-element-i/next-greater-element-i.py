class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greater = defaultdict(lambda: -1)
        stack = []

        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                greater[stack.pop()] = nums2[i]

            stack.append(nums2[i])

        return [greater[num] for num in nums1]