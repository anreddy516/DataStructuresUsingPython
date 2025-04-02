class MyQueue:
    
    # Create Queue constructor
    def __init__(self, capacity):        
        self.capacity = capacity
        self.rear = -1
        self.front = -1
        self.queue_items = [0] * self.capacity
    
    def is_queue_full(self):
        if (self.rear == self.capacity - 1):
            return True
        else:
            return False
    
    def is_queue_empty(self):
        if ((self.front == -1 and self.rear == -1) or (self.front > self.rear)):
            return True
        else:
            return False
    
    def enqueue(self, item):
        if (self.is_queue_full(self)):
            print("Queue is full or overflow")
            return False
        
        if (self.front == -1 and self.rear == -1):
            self.front = 0
            self.rear = 0
            self.queue_items [self.rear] = item
            return True
        else:
            self.rear = self.rear + 1
            self.queue_items [self.rear] = item
            return True
        
    def dequeue(self):
        if (self.isQueueEmpty()):
            print("Queue is empty or underflow")
            return -1

        item = self.queue_items[self.front]
        self.front = self.front + 1
        return item
    
    def peek(self):
        if (self.isQueueEmpty()):
            print("Queue is empty or underflow")
            return -1

        item = self.queue_items[self.front]
        return item
    
    def display_items_in_queue(self):
        print("Rear = " + self.rear)
        print("Front = " + self.front)
        print("Capacity = "+ self.capacity)
        print("Queue items are : ", end = "")
        if (self.is_queue_empty() != True):
            for i in range(self.front, self.rear + 1):
                print(self.queue_items[i], end=" ")

