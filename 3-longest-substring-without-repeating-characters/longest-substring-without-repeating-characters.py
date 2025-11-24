class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()
        leftIndex, rightIndex = 0, 0
        length_of_substring = 0
        temp_length = 0
        while rightIndex < len(s):
            if s[rightIndex] not in substring:
                temp_length += 1
                substring.add(s[rightIndex])
                rightIndex += 1
            else:
                if temp_length > length_of_substring:
                    length_of_substring = temp_length
                temp_length -= 1
                substring.remove(s[leftIndex])
                leftIndex += 1
        if temp_length > length_of_substring:
            length_of_substring = temp_length
        return length_of_substring