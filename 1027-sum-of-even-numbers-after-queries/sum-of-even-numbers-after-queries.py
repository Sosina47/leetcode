class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        total = sum(filter(lambda x: x % 2 == 0, nums))

        for i in range(len(queries)):
            n = nums[queries[i][1]]
            if n % 2 == 0:
                total -= n

            nums[queries[i][1]] += queries[i][0]
            n = nums[queries[i][1]] 
            if n % 2 == 0:
                total += n
            
            queries[i] = total

        return queries
