class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        chemistry = 0
        skill.sort()
        total_skill = skill[0] + skill[-1]

        left, right = 0, len(skill) - 1
        while right > left:
            if skill[right] + skill[left] != total_skill:
                return -1
            
            chemistry += skill[right] * skill[left]
            right -= 1
            left += 1

        return chemistry