class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        left, right = 0, len(people) - 1
        people.sort()
        count_boats = 0

        while right >= left:
            if people[right] + people[left] <= limit:
                left += 1
            
            count_boats += 1
            right -= 1

        return count_boats