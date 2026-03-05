class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        length = len(security)
        if time == 0:
            return [i for i in range(length)]

        possible = set()
        time_count = 0
        for i in range(length):
            if i == 0:
                if time_count >= time:
                    possible.add(i)
                time_count += 1

            else:
                if security[i] > security[i - 1]:
                    time_count = 0
                
                if time_count >= time:
                    possible.add(i)

                time_count += 1

        output = []
        time_count = 0
        for i in range(length - 1, -1, -1):
            if i == length - 1:
                if time_count >= time and i in possible:
                    output.append(i)
                time_count += 1

            else:
                if security[i] > security[i + 1]:
                    time_count = 0

                if time_count >= time and i in possible:
                    output.append(i)
                
                time_count += 1

        return output 