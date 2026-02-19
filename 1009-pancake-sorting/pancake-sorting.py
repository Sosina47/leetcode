class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        length = len(arr)
        sorted_arr = sorted(arr)
        output = []

        right_pos = length - 1
        while right_pos > 0:
            num = sorted_arr[right_pos]

            if arr[right_pos] != num:
                i = arr.index(num)

                if i > 0:
                    self.reverse_arr(arr, i)
                    output.append(i + 1) 

                self.reverse_arr(arr, right_pos)
                output.append(right_pos + 1)

            right_pos -= 1

        return output

    def reverse_arr(self, nums, end):
        left, right = 0, end 

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left, right = left + 1, right - 1
