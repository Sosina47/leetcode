class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        output = set()
        n = len(nums)

        def solve(start, subseq):
            
            if len(subseq) >= 2:
                output.add(tuple(subseq))

            for i in range(start, n):

                if not subseq or subseq[-1] <= nums[i]:
                    subseq.append(nums[i])

                    solve(i + 1, subseq)

                    subseq.pop()
                

        solve(0, [])
        return list(output)
