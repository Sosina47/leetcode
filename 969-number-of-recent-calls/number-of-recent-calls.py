class RecentCounter:

    def __init__(self):
        self.prev_calls = []        

    def ping(self, t: int) -> int:
        self.prev_calls.append(t) 
        low = t - 3000
        count_calls = 0
        
        for i in reversed(range(len(self.prev_calls))):
            if self.prev_calls[i] < low:
                break
            count_calls += 1


        return count_calls
        