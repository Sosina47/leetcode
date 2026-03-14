class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        freq = {20: 0, 10: 0, 5: 0}
        next = {20: 10, 10: 5, 5: -1} 

        for bill in bills:
            change = bill - 5  
            nxt = next[bill]
            freq[bill] += 1
            
            while change > 0:
                if freq[nxt] > 0:   
                    change -= nxt
                    print(change)
                    freq[nxt] -= 1

                    if 0 < change < nxt:
                        nxt = next[nxt]

                else:
                    nxt = next[nxt]
                
                if nxt == -1:
                    return False

        return True