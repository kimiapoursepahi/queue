#Queue
class Queue:
    def __init__(self, size):
        self.capacity = size
        self.queue = [None] * self.capacity
        self.front = 0
        self.rear = -1
        self.count = 0

    def enqueue(self, item):
        if self.is_full():
            print(f"Queue is full. Cannot enqueue {item}.")
            return
        self.rear += 1
        self.queue[self.rear] = item
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        item = self.queue[self.front]
        for i in range(1, self.count):
            self.queue[i - 1] = self.queue[i]
        self.queue[self.rear] = None
        self.rear -= 1
        self.count -= 1
        return item

    def peek(self):
        if self.is_empty():
            print("Queue is empty. Cannot peek.")
            return None
        return self.queue[self.front]

    def reverse_queue(self):
        if self.is_empty():
            print("Queue is empty. Cannot reverse.")
            return
        start, end = self.front, self.rear
        while start < end:
            self.queue[start], self.queue[end] = self.queue[end], self.queue[start]
            start += 1
            end -= 1

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.capacity

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        print("Queue elements:", end=" ")
        for i in range(self.count):
            print(self.queue[i], end=" ")
        print()

if __name__ == "__main__":
    q = Queue(5)

    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    q.enqueue(50)
    q.display()

    print("Front element:", q.peek())

    print("Dequeued element:", q.dequeue())
    q.display()

    q.enqueue(100)
    q.display()

    print("Dequeued element:", q.dequeue())
    q.display()

    print("Dequeued element:", q.dequeue())
    q.display()

    q.enqueue(200)
    q.display()

    print("Dequeued element:", q.dequeue())
    q.display()

    q.enqueue(300)
    q.display()


#CircularQueue
class CircularQueue:
    def __init__(self, size):
        self.capacity = size
        self.queue = [None] * self.capacity
        self.front = -1
        self.rear = -1

    def enqueue(self, item):
        if self.is_full():
            print(f"Queue is full. Cannot enqueue {item}.")
            return
        if self.is_empty():
            self.front = 0
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        item = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        return item

    def peek(self):
        if self.is_empty():
            print("Queue is empty. Cannot peek.")
            return None
        return self.queue[self.front]

    def reverse_queue(self):
        if self.is_empty():
            print("Queue is empty. Cannot reverse.")
            return
        start = self.front
        end = self.rear
        while start != end and (start + 1) % self.capacity != end:
            self.queue[start], self.queue[end] = self.queue[end], self.queue[start]
            start = (start + 1) % self.capacity
            end = (end - 1 + self.capacity) % self.capacity

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        print("Queue elements:", end=" ")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.capacity
        print()

if __name__ == "__main__":
    q = CircularQueue(5)

    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    q.enqueue(50)
    q.display()

    print("Front element:", q.peek())

    print("Dequeued element:", q.dequeue())
    q.display()

    q.enqueue(100)
    q.display()

    q.enqueue(200)
    q.display()

    print("Reversing the queue...")
    q.reverse_queue()
    q.display()