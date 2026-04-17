class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        n = len(instructions)

        for i in range(n):
            instructions[i] = (instructions[i], i)

        costs = defaultdict(lambda : [0, 0])

        def merge(left, right):
            nonlocal costs

            res = []
            l = r = 0
            
            len_r = len(right)
            len_l = len(left)

            while r < len(right):
                while l < len_l and left[l][0] <= right[r][0]:
                    l += 1

                costs[right[r]][1] += len_l - l
                r += 1

            l = r = 0

            while r < len_r:
                while l < len_l and left[l][0] < right[r][0]:
                    l += 1

                costs[right[r]][0] += l
                r += 1

            l = r = 0

            while r < len_r and l < len_l:
                if left[l][0] <= right[r][0]:
                    res.append(left[l])
                    l += 1

                else:
                    res.append(right[r])
                    r += 1

            res.extend(left[l: ])
            res.extend(right[r: ])

            return res
            

        def mergeSort(l, r):
            if l == r:
                return [instructions[l]]

            mid = (l + r) // 2

            left = mergeSort(l, mid) 
            right = mergeSort(mid + 1, r)

            return merge(left, right)


        mergeSort(0, n - 1)

        cost = 0
        for smaller, larger in costs.values():
            cost += min(smaller, larger)

        return cost % (10 ** 9 + 7)




