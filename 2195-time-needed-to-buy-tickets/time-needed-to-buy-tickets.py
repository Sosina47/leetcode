class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        tickets = deque(tickets)
        time_needed = 0
        index = 0

        while len(tickets) > 0:
            tickets[index] -= 1
            
            temp = tickets.popleft()
            if temp > 0:
                tickets.append(temp)
            time_needed += 1

            if k == 0 and temp == 0:
                return time_needed 

            if k == 0:
                k = len(tickets)
            
            k -= 1