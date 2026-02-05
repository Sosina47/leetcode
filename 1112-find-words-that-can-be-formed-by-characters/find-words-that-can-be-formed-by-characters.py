class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars = Counter(chars)
        length = 0

        for word in words:
            dict = Counter(word)

            for key, value in dict.items():
                if key not in chars or chars[key] < value:
                    break

            else:
                length += len(word)

        return length