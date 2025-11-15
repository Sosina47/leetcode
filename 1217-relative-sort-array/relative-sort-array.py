class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr2_index = {}
        for index, val in enumerate(arr2):
            arr2_index[val] = index

        i = 0
        numsNotInArr = []
        while i < len(arr1):
            if arr1[i] not in arr2:
                numsNotInArr.append(arr1[i])
                arr1.remove(arr1[i])
            else:
                i += 1

        for i in range(1, len(arr1)):
            j = i - 1
            key = arr1[i]
            while j >= 0 and arr2_index[arr1[j]] > arr2_index[key]:
                arr1[j + 1] = arr1[j] 
                j -= 1
            arr1[j + 1] = key
        numsNotInArr.sort()
        arr1.extend(numsNotInArr)
        
        return arr1