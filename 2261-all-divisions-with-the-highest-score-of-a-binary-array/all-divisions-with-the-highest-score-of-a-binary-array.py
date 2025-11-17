class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        count0 = nums.count(0)
        count1 = nums.count(1)
        numsSum = [[0, count1]]

        for i in range(1, len(nums)):
            if nums[i - 1] == 0:
                iCount0 = numsSum[i - 1][0] + 1
            else:
                iCount0 = numsSum[i - 1][0]

            if nums[i - 1] == 1:
                iCount1 = numsSum[i - 1][1] - 1
            else: 
                iCount1 = numsSum[i - 1][1]
            numsSum.append([iCount0, iCount1])

        scores = []
        for i in range(len(numsSum)):
            scores.append(sum(numsSum[i]))
        
        # for i == n, include all the zeros to the left of it
        scores.append(count0)
        
        max_score = max(scores)
        output = []
        for i in range(len(scores)):
            if scores[i] == max_score:
                output.append(i)

        return output
    