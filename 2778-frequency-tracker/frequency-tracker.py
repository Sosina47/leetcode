class FrequencyTracker:

    def __init__(self):
        self.arr = {}
        self.freq = {}
        
    def add(self, number: int) -> None:
        self.arr[number] = self.arr.get(number, 0) + 1
        val = self.arr[number]

        if val - 1 and val - 1 in self.freq:
            self.freq[val - 1] -= 1

        self.freq[val] = self.freq.get(val, 0) + 1
        
    def deleteOne(self, number: int) -> None:
        if number in self.arr and self.arr[number]:
            self.freq[self.arr[number]] -= 1 

            self.arr[number] -= 1     
            self.freq[self.arr[number]] = self.freq.get(self.arr[number], 0) + 1   

    def hasFrequency(self, frequency: int) -> bool:
        if frequency in self.freq and self.freq[frequency]:
                return True

        return False


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)