class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        prefix = []
        total = 0
        for i in range(len(arr)):
            if i == 0:
                prefix.append(arr[i])
            else:
                prefix.append(arr[i] + prefix[i - 1])

        for left in range(len(arr)):
            right = left
            while right < len(arr):
                if left == 0:
                    total += prefix[right]
                else:
                    total += prefix[right] - prefix[left - 1]
                right += 2
                
        return total