class DataStream:

    def __init__(self, value: int, k: int):
        self.stream = deque()
        self.val = value 
        self.k = k

    def consec(self, num: int) -> bool:
        self.stream.append(num)

        while self.stream and self.stream[-1] != self.val:
            self.stream.popleft()

        if len(self.stream) >= self.k:
            return True
        
        return False


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)