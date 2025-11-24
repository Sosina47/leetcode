class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count_subarray = 0
        left = 0
        cur_sum = 0

        for right in range(k):
            cur_sum += arr[right]
            
        if cur_sum / k >= threshold:
            count_subarray += 1 

        for right in range(k, len(arr)):
            print(arr[right])
            cur_sum -= arr[left]
            left += 1

            cur_sum += arr[right]
            if cur_sum / k >= threshold:
                count_subarray += 1
        
        return count_subarray  