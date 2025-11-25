class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruit_kind = {}
        left = right = 0
        max_fruit = 0

        while right < len(fruits):
            while fruits[right] not in fruit_kind and len(fruit_kind) >= 2:
                if fruit_kind[fruits[left]] == 1:
                    fruit_kind.pop(fruits[left])
                else:
                    fruit_kind[fruits[left]] -= 1
                left += 1

            if fruits[right] in fruit_kind:
                fruit_kind[fruits[right]] += 1
            else:
                fruit_kind[fruits[right]] = 1
            max_fruit = max(max_fruit, right - left + 1)

            right += 1

        return max_fruit