class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        count_boat = 0
        people.sort(reverse=True)

        left, right = 0, len(people) - 1
        while left <= right:
            if people[left] + people[right] <= limit:
                right -= 1
            left += 1
            count_boat += 1

        return count_boat