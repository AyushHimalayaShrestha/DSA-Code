class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, data):
        self.queue.append(data)
    
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return "Queue is empty"
    
    def is_empty(self):
        return len(self.queue) == 0

# Example Usage
if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(5)
    queue.enqueue(10)
    print(queue.dequeue())  
