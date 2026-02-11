class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        max_ = 0
        word = ''

        count = defaultdict(int)
        for response in responses:
            seen = set()

            for r in response:
                if r not in seen:
                    count[r] += 1
                    max_ = max(max_, count[r])
                    seen.add(r)

        for response in count:
            if count[response] == max_:

                if not word:
                    word = response
                else:
                    word = min(word, response)

        return word