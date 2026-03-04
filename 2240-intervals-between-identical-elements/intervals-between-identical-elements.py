class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        indices = defaultdict(list)
        intervals = {}
        for i in range(len(arr)):
            indices[arr[i]].append(i)

        for key, val in indices.items():
            prefix = [val[0]]

            # prefix sum
            for i in range(1, len(val)):
                prefix.append(val[i] + prefix[i - 1])
            
            total = prefix[-1]
            prefix.append(0)
            new_prefix = []

            for i in range(len(val)):
                left = i * val[i] - prefix[i - 1] # values before the current element 
                right = total - prefix[i] - (len(val) - 1 - i) * val[i] # values after the current element

                new_prefix.append(left + right)
            intervals[key] = new_prefix 
            
        count_idx = defaultdict(int)
        for i in range(len(arr)):
            key = arr[i]
            arr[i] = intervals[key][count_idx[key]]
            count_idx[key] += 1

        return arr 