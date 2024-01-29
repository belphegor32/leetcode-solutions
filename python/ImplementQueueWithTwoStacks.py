class MyQueue(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        # We only append to stack1, because we will then move them to stack2 if needed
        self.stack1.append(x)
    
        

    def pop(self):
        # Add numbers to stack two
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        # Since values in stack2 are reversed, we can just pop from top
        return self.stack2.pop()
        

    def peek(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        # Since values in stack2 are reversed, we can just return the value from the top
        return self.stack2[-1]
        

    def empty(self):
        # If both stacks are empty we can return True, else False
        return max(len(self.stack1), len(self.stack2)) == 0