class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []        
        
        length1 = len(firstList)
        length2 = len(secondList)

        result = []

        left = right = 0
        while left < length1 and right < length2:
            temp = [0, 0]
            temp[0] = max(firstList[left][0], secondList[right][0])
            temp[1] = min(firstList[left][1], secondList[right][1])

            if temp[0] <= temp[1]:
                result.append(temp)

            if firstList[left][1] > secondList[right][1]:
                right += 1
            elif firstList[left][1] < secondList[right][1]:
                left += 1
            else:
                left += 1
                right += 1
        
        return result
    