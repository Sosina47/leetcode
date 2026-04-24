class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        cover = defaultdict(list)
        bombs = list(map(tuple, bombs))

        def inRange(b, i, r): 
            dis = sqrt((b[0] - i[0]) ** 2 + (b[1] - i[1]) ** 2)

            return r >= dis
            

        for j in range(n):
            for i in range(n):

                if inRange(bombs[j], bombs[i], bombs[j][2]):
                    cover[j].append(i)

        count = 0
        for b in cover:
            cur = 0
            visited = set()

            que = deque([b])
            visited.add(b) 

            while que:
                node = que.popleft()

                cur += 1
                for n in cover[node]:

                    if n not in visited: 
                        que.append(n)
                        visited.add(n)
                
            count = max(count, cur)

        return count
                    