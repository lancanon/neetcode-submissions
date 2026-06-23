class MinStack:

    def __init__(self):
        # This is the regular stack to store all values
        self.stack = []
        # This is the special "min stack" to track current minimums
        self.minStack = []
        
    def push(self, val: int) -> None:
        # Push the value to the main stack
        self.stack.append(val)

        # Compare the new value with the current min value (top of minStack)
        # Push the smaller one to minStack
        # If minStack is empty, just push val
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)
        

    def pop(self) -> None:
        # Pop from both stacks to keep them in sync
        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        # Top of the minStack is always the current minimum
        return self.minStack[-1]
        
