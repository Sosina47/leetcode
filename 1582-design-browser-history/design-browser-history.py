class Node:
    def __init__(self, val, previous = None, next = None):
        self.val = val
        self.previous = previous
        self.next = next

class BrowserHistory(Node):
    def __init__(self, homepage: str):
        node = Node(homepage)
        self.head = node
        self.tail = node

    def visit(self, url: str) -> None:
        node = Node(url, self.tail)
        self.tail.next = node
        self.tail = node
    
    def back(self, steps: int) -> str:
        count = 0

        while count < steps and self.tail is not self.head:
            self.tail = self.tail.previous
            count += 1

        return self.tail.val

    def forward(self, steps: int) -> str:
        count = 0
        while count < steps and self.tail.next:
            self.tail = self.tail.next
            count += 1

        return self.tail.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)