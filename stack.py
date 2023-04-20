class Stack:
    def __init__(self, *args) -> None:
        if args:
            self.stack = list(args)
        else:
            self.stack = []
    
    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]
    
