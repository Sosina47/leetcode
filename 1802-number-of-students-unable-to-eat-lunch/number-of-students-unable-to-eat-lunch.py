class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        q = deque(students)
        count_didnt_eat = 0
        sandwiches.reverse()

        while q:
            student = q.popleft()
            if student == sandwiches[-1]:
                sandwiches.pop()
                count_didnt_eat = 0
            else:
                q.append(student)
                count_didnt_eat += 1

            if count_didnt_eat == len(q):
                return count_didnt_eat
            