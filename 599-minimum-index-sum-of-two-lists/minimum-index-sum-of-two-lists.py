class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dict_2 = {val: index for index, val in enumerate(list2)}

        output = []
        min_index = float('inf')

        for i in range(len(list1)):
            if list1[i] in dict_2:
                index = i + dict_2[list1[i]]
                
                if index == min_index:
                    output.append(list1[i])
                elif index < min_index:
                    output = [list1[i]]
                    min_index = index

        return output