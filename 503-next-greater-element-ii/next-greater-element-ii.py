class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        length = len(nums)
        greater = defaultdict(lambda: -1)
        stack = []

        for i in range(2 * length):
            while stack and nums[stack[-1]] < nums[i % length]:
                greater[stack.pop()] = i % length

            stack.append(i % length)

        print(greater)

        output = []
        for i in range(length):
            if greater[i] != -1:
                output.append(nums[greater[i]])
            else:
                output.append(-1)
            

        return output