class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Push the minimum value onto the minstack.
        # If the minstack is empty, or the new value is smaller than the current minimum,
        # push the new value onto minstack.
        # Otherwise, push the current minimum again to maintain the correct minimum value at this level.( same length)
        self.minstack.append(val if not self.minstack or val< self.minstack[-1] else self.minstack[-1])

    def pop(self) -> None:
        
        self.minstack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()