class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        
        self.stack.append(val)

    def pop(self) -> None:
        
        n = len(self.stack)
        if n == 1 or n == 0:
            self.stack = []
            return
        self.stack = self.stack[:-1]

    def top(self) -> int:
        print(self.stack)
        return self.stack[-1]
        

    def getMin(self) -> int:
        return min(self.stack)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()