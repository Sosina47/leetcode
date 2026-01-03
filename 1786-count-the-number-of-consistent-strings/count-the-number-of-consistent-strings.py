class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        result = 0

        for word in words:
            count = Counter(word)
            is_in = True
            for letter in count:
                if letter not in allowed:
                    is_in = False
                    break

            if is_in:
                result += 1 

        return result