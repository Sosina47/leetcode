class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        smaller = defaultdict(int)
        
        for i in range(len(nums)):
            nums[i] = (nums[i], i)


        def mergeSort(left, right):
            if left == right:
                return [nums[left]]

            mid = left + (right - left) // 2

            left_arr = mergeSort(left, mid)
            right_arr = mergeSort(mid + 1, right)

            return merge(left_arr, right_arr)

        def merge(left, right):
            result = []

            l = r = 0

            while l < len(left) and r < len(right):

                if left[l][0] > right[r][0]:
                    smaller[left[l]] += len(right) - r 

                    result.append(left[l])
                    l += 1

                else:
                    result.append(right[r])
                    r += 1

            result.extend(left[l:])
            result.extend(right[r:])

            return result


        mergeSort(0, len(nums) - 1)

        for i in range(len(nums)):
            nums[i] = smaller[nums[i]]

        return nums