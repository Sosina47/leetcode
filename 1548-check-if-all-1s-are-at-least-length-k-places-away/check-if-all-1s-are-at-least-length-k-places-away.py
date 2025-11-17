class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prev_one = 0
        oneBefore = False
        for i in range(len(nums)):
            if nums[i] == 1:
                if not oneBefore:
                    prev_one = i
                    oneBefore = True
                else:
                    if i - prev_one - 1 < k:
                        return False
                    else:
                        prev_one = i
                
        return True