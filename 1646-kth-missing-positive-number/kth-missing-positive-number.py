class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        j = 1
        count_missing = 0
        i = 0
        while i < len(arr):
            if arr[i] != j:
                count_missing += 1
                if count_missing == k:
                    return j
                j += 1
                print(arr[i], j, count_missing)
            else:
                i += 1
                j += 1
        j -= 1
        while count_missing < k:
            j += 1
            print(j, count_missing)
            count_missing += 1
        return j