class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domains = defaultdict(int)
        
        for cpdomain in cpdomains:
            lst = list(cpdomain.split())

            domains[lst[1]] += int(lst[0])
            idx = lst[1].find('.')

            while idx != -1:
                lst[1] = lst[1][idx + 1:]
                domains[lst[1]] += int(lst[0])
                idx = lst[1].find('.')

        output = []
        for key, value in domains.items():
            output.append(f"{value} {key}")

        return output
