class MyStack: 
    
    # Create stack or initialize a stack with some capacity
    
    def __init__(self, capacity):
        self.capacity =  capacity
        self.top = -1
        self.stack_storage = [0] * self.capacity
    
    # is_stack_full() or stack overflow - when stack is full
    def is_stack_full(self):
        if (self.top == self.capacity - 1):
            return True
        else:
            return False
        
    # is_stack_empty() or stack underflow - when stack is empty.
    def is_stack_empty(self):
        if (self.top == -1):
            return True
        else:
            return False
    
    # push() - to add an item at top of a stack
    def push(self, item):
        if (self.is_stack_full()):
            print("Stack is overflow")
            return False
        
        self.top = self.top + 1
        self.stack_storage[self.top] = item
        return True

    # Retrieve an item from top
    def pop(self):
        if (self.is_stack_empty()):
            print("Stack is underflow or empty")
            return -1
        
        item = self.stack_storage[self.top]
        self.top = self.top - 1
        return item
    
    # Get an item from top
    def peek(self):
        if (self.is_stack_empty()):
            print("Stack is underflow or empty")
            return -1
        
        item = self.stack_storage[self.top]
        return item
    
    def print(self):
        print(f"Capacity = {self.capacity}")
        print(f"Top      = {self.top}")
        print("Stack items are here:")
        for i in range(self.top, -1, -1) :
            print(self.stack_storage[i])
        