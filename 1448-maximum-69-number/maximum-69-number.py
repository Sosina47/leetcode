class Solution:
    def maximum69Number (self, num: int) -> int:
        num_list = [digit for digit in str(num)]
        for i in range(len(num_list)):
            integer = int(num_list[i])
            if integer < 9:
                num_list[i] = '9'
                break
        return int(''.join(num_list))
    