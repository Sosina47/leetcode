class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []

        def dfs(i, subs):
            if i == n: 
                res.append(subs[::])
                return 

            for j in range(i, n): 
                cur = s[i:j + 1]

                if cur == cur[::-1]:
                    subs.append(cur)

                    dfs(j + 1, subs)

                    subs.pop()


        dfs(0, [])
        return res