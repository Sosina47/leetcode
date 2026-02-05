class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        min_sum = float('inf')
        output = []

        for i in range(len(list1)):
            if list1[i] not in list2:
                continue

            idx = list2.index(list1[i]) + i 

            if idx == min_sum:
                output.append(list1[i])

            elif idx < min_sum:
                output = [list1[i]]
                min_sum = idx

        return output