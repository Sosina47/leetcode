class Solution():
    def answerQueries(self, nums: List[int], queries: List[int]):
        nums.sort()
        length = len(nums)
        
        # prefix sum
        for index in range(1, length):
            nums[index] = nums[index] + nums[index - 1]
        
        answer = []
        for qIndex in range(len(queries)):
            for nIndex in range(length):
                if nums[nIndex] > queries[qIndex]:
                    answer.append(nIndex)
                    break
                
                if nIndex == length - 1 and nums[nIndex] <= queries[qIndex]:
                    answer.append(nIndex + 1)
        return answer
    