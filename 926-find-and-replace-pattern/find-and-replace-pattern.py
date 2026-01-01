class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        result = []
        for word in words:
            mapping = {}
            is_match = True
            for i in range(len(word)):
                if word[i] in mapping:
                    if pattern[i] != mapping[word[i]]:
                        is_match = False
                        break
                elif pattern[i] in mapping.values():
                    is_match = False
                    break
                else:
                    mapping[word[i]] = pattern[i]

            if is_match:
                result.append(word)

        return result