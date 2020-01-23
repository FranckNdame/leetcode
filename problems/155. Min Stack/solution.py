class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minimum = float('inf')

    def push(self, x: int) -> None:
        self.minimum = min(self.minimum, x)
        self.stack.append((x, self.minimum))

    def pop(self) -> None:
        if not self.stack:
            return
        self.stack.pop()
        if not self.stack:
            self.minimum = float('inf')
        else:
            self.minimum = self.stack[-1][1]

    def top(self) -> int:
        if not self.stack:
            return
        return self.stack[-1][0]

    def getMin(self) -> int:
        if not self.stack:
            return
        return self.minimum


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
