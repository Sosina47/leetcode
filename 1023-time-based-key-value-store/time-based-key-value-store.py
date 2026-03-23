class TimeMap:

    def __init__(self):
        self.hash = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash[key].append((value, timestamp))        

    def get(self, key: str, timestamp: int) -> str:
        vals = self.hash[key]
        
        left = 0
        right = len(vals) - 1
        
        while right >= left:
            mid = (right + left) // 2
            val = vals[mid][1]

            if val == timestamp:
                return vals[mid][0]

            elif val < timestamp:
                left = mid + 1
            
            else:
                right = mid - 1

        return vals[right][0] if right >= 0 else ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)