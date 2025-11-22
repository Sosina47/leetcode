class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        
        i, j = 1, len(skill) - 2
        prev_skill = skill[0] + skill[-1]
        chemistry = skill[0] * skill[-1]
        while i <= j:
            skill_product = skill[i] * skill[j]
            skill_sum = skill[i] + skill[j]

            if skill_sum != prev_skill:
                return -1
            chemistry += skill_product
            i += 1
            j -= 1
        
        return chemistry
