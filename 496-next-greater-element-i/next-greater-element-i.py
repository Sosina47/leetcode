class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        length = len(nums2)
        result = [-1] * length

        for i in range(length - 1, -1, -1):
            num = nums2[i]

            while stack and stack[-1] <= num:
                stack.pop()
            
            if stack:
                result[i] = stack[-1]
            
            stack.append(num)

        position = {nums2[i]: i for i in range(length)}

        for i in range(len(nums1)):
            nums1[i] = result[position[nums1[i]]]

        return nums1
